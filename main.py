"""
Usage:
    script_name.py [-a] [-b] <query>...

Options:
    -a            Print all the things.
    -b            Get more bees into the path.
"""
from typing import Any, List, Type
from docopt import docopt
import requests
from bs4 import BeautifulSoup

from selectors.basic_selector import BasicSelector
from selectors.currency_selector import CurrencySelector
from selectors.math_selector import MathSelector
from selectors.selector import Selector
from selectors.site_list_selector import WebsiteResultSelector2
from selectors.site_selector import WebsiteResultSelector


def get_page(query: List[str]):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.15.2 "
                      "Chrome/87.0.4280.144 Safari/537.36"}

    response = requests.get(f'https://www.google.com/search',
                            params={"q": " ".join(query)},
                            headers=headers
                            )

    return BeautifulSoup(response.content, 'html.parser')


if __name__ == "__main__":
    args = docopt(__doc__)
    # import pprint; pprint.pprint(args)
    doc = get_page(args['<query>'])
    print(doc.title)

    clazz: List[Type[Selector]] = [BasicSelector, MathSelector, CurrencySelector, WebsiteResultSelector,
                                   WebsiteResultSelector2]

    for claz in clazz:
        selector = claz(doc)
        if selector.found():
            selector.display()