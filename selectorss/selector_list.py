from typing import List, Type

from .basic_selector import BasicSelector
from .currency_selector import CurrencySelector
from .math_selector import MathSelector
from .selector import Selector
from .site_list_selector import WebsiteResultSelector2
from .site_selector import WebsiteResultSelector

selector_classes: List[Type[Selector]] = [
    BasicSelector,
    MathSelector,
    CurrencySelector,
    WebsiteResultSelector,
    WebsiteResultSelector2
]
