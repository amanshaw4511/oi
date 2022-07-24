from typing import List, Mapping, Optional, Type
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


def get_page(query: List[str]):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.15.2 "
                      "Chrome/87.0.4280.144 Safari/537.36"}

    response = requests.get(f'https://www.google.com/search',
                            params={"q": " ".join(query)},
                            headers=headers
                            )

    return BeautifulSoup(response.content, 'html.parser')

def print_availabe_selectors():
    configs_json = json.loads(open('./config/config.json').read())
    configs = map(Config, configs_json)

    for config in configs:
        print(config.selector, end=' ')

    print()


def main():
    args = get_args()
    query: List[str] = args['<query>']
    selector_name: Optional[str] = args['--selector']
    list_selector: bool = args['--list-selectors']

    if list_selector :
        print_availabe_selectors()
        return
    

    doc = get_page(query)
    # print(doc.title)

    clazz: List[Type[Selector]] = [BasicSelector, MathSelector, CurrencySelector, WebsiteResultSelector,
                                   WebsiteResultSelector2]

    for claz in clazz:
        obj = claz(doc)
        if obj.found():
            obj.display()


if __name__ == "__main__":
    main()
