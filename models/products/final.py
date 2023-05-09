from enum import Enum

from models.products.raw import Product

from models.products.middle_two import MiddleLevelTwoList


class Final(Product):
    def __init__(self, name, volume, min_price, max_price, dependencies={}, production_rate=None, fixed_cost=None, variable_cost=None):
        super().__init__(name, volume, min_price, max_price, dependencies, production_rate, fixed_cost, variable_cost)


class FinalList(Enum):
    GPhone1 = Final("GPhone1", 1127, 61500, 88500, {MiddleLevelTwoList.Communication2G: 1, MiddleLevelTwoList.MediaNoCamera: 1, MiddleLevelTwoList.PhoneBody1: 1}, 200, 11972598, 8246)
    GPhone2 = Final("GPhone2", 503, 68800, 98600, {MiddleLevelTwoList.Communication3G: 1, MiddleLevelTwoList.MediaSingleCamera: 1, MiddleLevelTwoList.PhoneBody2: 1}, 300, 18300692, 9950)
    GPhone3 = Final("GPhone3", 555, 75200, 111000, {MiddleLevelTwoList.Communication3G: 1, MiddleLevelTwoList.MediaSingleCamera: 1, MiddleLevelTwoList.PhoneBody2: 1}, 130, 11840669, 9452)
