from typing import List, Type, Any

from selectors.selector import Selector
from utils.list import find_any


class Config:
    def __init__(self, _dict: Any, selector_classes: List[Type[Selector]]):
        self.selector: str = _dict.get('selector')
        self.id: str = _dict.get('id')
        self.query: List[str] = _dict.get('query')
        self.comment: str = _dict.get('comment')
        self.clazz = find_any(lambda clazz: clazz.name == self.selector, selector_classes)
