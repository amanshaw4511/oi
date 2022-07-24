from bs4 import BeautifulSoup

from .selector import Selector


class CurrencySelector(Selector):
    name = "currency"

    def __init__(self, doc: BeautifulSoup):
        self.selector = 'div.dDoNo.ikb4Bb.gsrt.GDBPqd'
        self.selected = doc.select(self.selector)

    def display(self):
        print(self.fetch())

    def fetch(self) -> str:
        return self.selected[0].text

    def found(self) -> bool:
        return len(self.selected) != 0
