from enum import Enum

from models.products.raw import Product

from models.products.middle_one import MiddleLevelOneList
from models.products.raw import RawMaterialList


class MiddleLevelTwo(Product):
    def __init__(self, name, volume, min_price, max_price, dependencies={}, production_rate=None, fixed_cost=None, variable_cost=None):
        super().__init__(name, volume, min_price, max_price, dependencies, production_rate, fixed_cost, variable_cost)


class MiddleLevelTwoList(Enum):
    Communication2G = MiddleLevelTwo("Communication2G", 100, 6000, 11300, {MiddleLevelOneList.Modem2G: 1, RawMaterialList.Chips: 1, RawMaterialList.Microphone: 1, }, 70, 480688, 830)
    MediaNoCamera = MiddleLevelTwo("MediaNoCamera", 19, 3500, 8200, {RawMaterialList.Speaker: 8}, 60, 1021727, 800)
    PhoneBody1 = MiddleLevelTwo("PhoneBody1", 1008, 23200, 34600, {MiddleLevelOneList.PhoneBattery: 1, MiddleLevelOneList.PhoneKeypad: 1, RawMaterialList.Ports: 1, RawMaterialList.VibrationMotor: 1}, 70, 2260571, 4115)
    Communication3G = MiddleLevelTwo("Communication3G", 152, 8600, 15400, {MiddleLevelOneList.Modem3G: 1, RawMaterialList.Chips: 2, RawMaterialList.Microphone: 2, }, 90, 1022404, 1365)
    MediaSingleCamera = MiddleLevelTwo("MediaSingleCamera", 203, 6900, 11400, {MiddleLevelOneList.Camera: 1, RawMaterialList.Speaker: 10}, 150, 1235507, 1238)
    PhoneBody2 = MiddleLevelTwo("PhoneBody2", 200, 26300, 34700, {MiddleLevelOneList.PhoneBattery: 1, MiddleLevelOneList.PhoneFrame: 1, MiddleLevelOneList.TouchDisplay: 1, RawMaterialList.Ports: 2, RawMaterialList.VibrationMotor: 1}, 290, 10027016, 4952)
