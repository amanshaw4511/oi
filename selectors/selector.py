from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup


class Selector(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, doc: BeautifulSoup):
        pass

    @abstractmethod
    def found(self) -> bool:
        pass

    @abstractmethod
    def display(self):
        pass
