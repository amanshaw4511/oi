from bs4 import BeautifulSoup

from .selector import Selector


class BasicSelector(Selector):
    name = "basic"

    def __init__(self, doc: BeautifulSoup, selector_id: str):
        self.selector = selector_id
        self.selected = doc.select(self.selector)

    def display(self):
        print(self.fetch())

    def fetch(self) -> str:
        return self.selected[0].text

    def found(self) -> bool:
        return len(self.selected) != 0
