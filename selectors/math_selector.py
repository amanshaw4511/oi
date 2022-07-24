from selector import Selector
from bs4 import BeautifulSoup


class MathSelector(Selector):
    def __init__(self, doc: BeautifulSoup):
        self.selector = 'span.qv3Wpe'
        self.selected = doc.select(self.selector)

    def display(self):
        print(self.fetch())

    def fetch(self) -> str:
        return self.selected[0].text

    def found(self) -> bool:
        return len(self.selected) != 0