from typing import List, Type, Any

from bs4 import BeautifulSoup

from selectorss.selector import Selector
from utils.list import find_any


class Config:
    def __init__(self, _dict: Any, selector_classes: List[Type[Selector]], doc: BeautifulSoup):
        self.name: str = _dict.get('selector')
        self.id: str = _dict.get('id')
        self.query: List[str] = _dict.get('query')
        self.comment: str = _dict.get('comment')

        _clazz = find_any(lambda clazz: clazz.name == self.name, selector_classes)
        assert _clazz is not None
        self.selector = _clazz(doc, self.id)
