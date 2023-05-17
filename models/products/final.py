from enum import Enum

from models.products.raw import Product

from models.products.middle_two import MiddleLevelTwoList


class Final(Product):
    def __init__(self, name, volume, min_price, max_price, dependencies={}, production_rate=None, fixed_cost=None, variable_cost=None):
        super().__init__(name, volume, min_price, max_price, dependencies, production_rate, fixed_cost, variable_cost)


class FinalList(Enum):
    GPhone1 = Final("GPhone1", 1127, 20740, 25340, {MiddleLevelTwoList.Communication2G: 1, MiddleLevelTwoList.MediaNoCamera: 1, MiddleLevelTwoList.PhoneBody1: 1}, 200, 5_570_000, 2760)
    GPhone2 = Final("GPhone2", 503, 20550, 25110, {MiddleLevelTwoList.Communication2G: 1, MiddleLevelTwoList.MediaSingleCamera: 1, MiddleLevelTwoList.PhoneBody2: 1}, 330, 8_870_000, 2975)
    GPhone3 = Final("GPhone3", 555, 22780, 27840, {MiddleLevelTwoList.Communication3G: 1, MiddleLevelTwoList.MediaSingleCamera: 1, MiddleLevelTwoList.PhoneBody2: 1}, 140, 4_100_000, 2850)
