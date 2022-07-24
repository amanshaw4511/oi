import sys
from typing import Iterable, List, Optional, Type, cast
import requests
from bs4 import BeautifulSoup
import json
from config.config import Config

from selectors.basic_selector import BasicSelector
from selectors.currency_selector import CurrencySelector
from selectors.math_selector import MathSelector
from selectors.selector import Selector
from selectors.site_list_selector import WebsiteResultSelector2
from selectors.site_selector import WebsiteResultSelector
from arg_parser.arg_parser import get_args
from utils.list import find_any
from utils.termcolor import red, bold

selector_classes: List[Type[Selector]] = [
        BasicSelector,
        MathSelector,
        CurrencySelector,
        WebsiteResultSelector,
        WebsiteResultSelector2
    ]


def get_page(query: List[str]):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.15.2 "
                      "Chrome/87.0.4280.144 Safari/537.36"}

    response = requests.get(f'https://www.google.com/search',
                            params={"q": " ".join(query)},
                            headers=headers
                            )

    return BeautifulSoup(response.content, 'html.parser')


def load_configs(config_path: str) -> Iterable[Config]:
    config_json = open(config_path).read()
    configs_dict = json.loads(config_json)
    return map(lambda x : Config(x, selector_classes), configs_dict)


def print_availabe_selectors(configs: Iterable[Config]):
    for config in configs:
        print(config.selector, end=' ')

    print()


def print_output_from_selector(doc: BeautifulSoup, selector_name: str) -> bool:
    selector_class = find_any(lambda clazz: clazz.name == selector_name, selector_classes)
    if not selector_class:
        print(red(f"Invalid selector name '{bold(selector_name)}'"), file=sys.stderr)
        return False

    selector_obj = selector_class(doc)
    if selector_obj.found():
        selector_obj.display()
        return True
    return False

def print_output_from_any_matched_selector(doc: BeautifulSoup):
    for selector_class in selector_classes:
        selector_obj = selector_class(doc)
        if selector_obj.found():
            selector_obj.display()
            return



def main():
    args = get_args()

    configs: Iterable[Config] = load_configs('./config/config.json')

    query: List[str] = args['<query>']
    selector_name: Optional[str] = args['--selector']
    list_selector: bool = args['--list-selectors']
    doc = get_page(query)

    if list_selector:
        print_availabe_selectors(configs)
        return

    if selector_name:
        flag = print_output_from_selector(doc, selector_name)
        if flag :
            return

    print_output_from_any_matched_selector(doc)



if __name__ == "__main__":
    main()

