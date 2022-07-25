import json
import sys
from typing import Iterable, List, Optional, Type

import requests
from bs4 import BeautifulSoup

from arg_parser.arg_parser import get_args
from config.config import Config
from selectors.selector import Selector
from utils.list import find_any
from utils.termcolor import red, bold


def get_page(query: List[str]):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.15.2 "
                      "Chrome/87.0.4280.144 Safari/537.36"}

    response = requests.get(f'https://www.google.com/search',
                            params={"q": " ".join(query)},
                            headers=headers
                            )

    return BeautifulSoup(response.content, 'html.parser')


def load_configs(config_path: str, doc: BeautifulSoup, selector_classes: List[Type[Selector]]) -> List[Config]:
    config_json = open(config_path).read()
    configs_dict = json.loads(config_json)
    return list(map(lambda x: Config(x, selector_classes, doc), configs_dict))


def print_available_selectors(configs: Iterable[Config]):
    for config in configs:
        print(config.name, end=' ')

    print()


def configs_to_selectors(configs: Iterable[Config]) -> Iterable[Selector]:
    return map(lambda config: config.selector, configs)


def print_output_from_selector(selector_name: str, configs: Iterable[Config]) -> bool:
    selector = find_any(lambda sel: sel.name == selector_name, configs_to_selectors(configs))

    if not selector:
        print(red(f"Invalid selector name '{bold(selector_name)}'"), file=sys.stderr)
        return False

    if selector.found():
        selector.display()
        return True
    return False


def print_output_from_any_matched_selector(configs: Iterable[Config]):
    for selector in configs_to_selectors(configs):
        if selector.found():
            selector.display()
            return


def main():
    from selectors.selector_list import selector_classes
    args = get_args()

    query: List[str] = args['<query>']
    selector_name: Optional[str] = args['--selector']
    list_selector: bool = args['--list-selectors']

    doc = get_page(query)

    configs: Iterable[Config] = load_configs('./config/config.json', doc, selector_classes)

    if list_selector:
        print_available_selectors(configs)
        return

    if selector_name:
        flag = print_output_from_selector(selector_name, configs)
        if flag:
            return

    print_output_from_any_matched_selector(configs)


if __name__ == "__main__":
    main()
