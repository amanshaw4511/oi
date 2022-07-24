from typing import List, Type
import requests
from bs4 import BeautifulSoup

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


def main():
    args = get_args()
    doc = get_page(args['<query>'])
    # print(doc.title)

    clazz: List[Type[Selector]] = [BasicSelector, MathSelector, CurrencySelector, WebsiteResultSelector,
                                   WebsiteResultSelector2]

    for claz in clazz:
        selector = claz(doc)
        if selector.found():
            selector.display()


if __name__ == "__main__":
    main()
