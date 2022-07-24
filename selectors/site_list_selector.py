from selector import Selector
from bs4 import BeautifulSoup


class WebsiteResultSelector2(Selector):
    def __init__(self, doc: BeautifulSoup):
        heading_selector = 'div.co8aDb'
        rows_selector = 'li.TrT0Xe'
        self.heading = doc.select(heading_selector)
        self.rows = doc.select(rows_selector)

    def display(self):
        heading, rows = self.fetch()
        print(heading)
        for row in rows:
            print(row)

    def fetch(self):
        return self.heading[0].text, map(lambda x: x.text, self.rows)

    def found(self) -> bool:
        return len(self.heading) != 0
