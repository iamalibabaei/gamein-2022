from enum import Enum

from models.products.raw import Product

from models.products.middle_one import MiddleLevelOneList
from models.products.raw import RawMaterialList


class MiddleLevelTwo(Product):
    def __init__(self, name, volume, min_price, max_price, dependencies={}, production_rate=None, fixed_cost=None, variable_cost=None):
        super().__init__(name, volume, min_price, max_price, dependencies, production_rate, fixed_cost, variable_cost)


class MiddleLevelTwoList(Enum):
    Communication2G = MiddleLevelTwo("Communication2G", 100, 2810, 3190, {MiddleLevelOneList.Modem2G: 1, RawMaterialList.Chips: 1, RawMaterialList.Microphone: 1, }, 80, 200_000, 284)
    MediaNoCamera = MiddleLevelTwo("MediaNoCamera", 19, 1470, 1670, {RawMaterialList.Speaker: 8}, 60, 30_000, 200)
    PhoneBody1 = MiddleLevelTwo("PhoneBody1", 1008, 9320, 10590, {MiddleLevelOneList.DisplayKeypad: 1, MiddleLevelOneList.PhoneBattery: 1, MiddleLevelOneList.PhoneKeypad: 1, RawMaterialList.Ports: 1, RawMaterialList.VibrationMotor: 1}, 70, 790_000, 1359)
    Communication3G = MiddleLevelTwo("Communication3G", 152, 3870, 4400, {MiddleLevelOneList.Modem3G: 1, RawMaterialList.Chips: 2, RawMaterialList.Microphone: 2, }, 100, 420_000, 477)
    MediaSingleCamera = MiddleLevelTwo("MediaSingleCamera", 203, 2430, 2760, {MiddleLevelOneList.Camera: 1, RawMaterialList.Speaker: 10}, 170, 450_000, 337)
    PhoneBody2 = MiddleLevelTwo("PhoneBody2", 200, 8280, 9410, {MiddleLevelOneList.PhoneBattery: 1, MiddleLevelOneList.PhoneFrame: 1, MiddleLevelOneList.TouchDisplay: 1, RawMaterialList.Ports: 2, RawMaterialList.VibrationMotor: 1}, 310, 3_470_000, 1410)
