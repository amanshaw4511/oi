from abc import ABCMeta, abstractmethod

from bs4 import BeautifulSoup


class Selector(metaclass=ABCMeta):
    name = ""

    @abstractmethod
    def __init__(self, doc: BeautifulSoup, selector_id: str):
        pass

    @abstractmethod
    def found(self) -> bool:
        pass

    @abstractmethod
    def display(self):
        pass
