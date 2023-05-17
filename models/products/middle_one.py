from enum import Enum

from models.products.raw import Product, RawMaterialList


class MiddleLevelOne(Product):
    def __init__(self, name, volume, min_price, max_price, dependencies={}, production_rate=None, fixed_cost=None, variable_cost=None):
        super().__init__(name, volume, min_price, max_price, dependencies, production_rate, fixed_cost, variable_cost)


class MiddleLevelOneList(Enum):
    Modem2G = MiddleLevelOne("Modem 2G", 80, 780, 1020, {RawMaterialList.Aluminium: 15, RawMaterialList.Copper: 10, RawMaterialList.Plastic: 30}, 100, 50_000, 50)
    DisplayKeypad = MiddleLevelOne("DisplayKeypad", 328, 1260, 1640, {RawMaterialList.Aluminium: 30, RawMaterialList.Glass: 150, RawMaterialList.Silicon: 50}, 80, 70_000, 93)
    PhoneBattery = MiddleLevelOne("PhoneBattery", 240, 660, 860, {RawMaterialList.Cobalt: 18, RawMaterialList.Lithium: 12, }, 210, 190_000, 61)
    PhoneKeypad = MiddleLevelOne("PhoneKeypad", 592, 1730, 2240, {RawMaterialList.Aluminium: 70, RawMaterialList.Plastic: 300}, 80, 200_000, 174)
    Camera = MiddleLevelOne("Camera", 224, 670, 870, {RawMaterialList.Copper: 20, RawMaterialList.Glass: 40, RawMaterialList.Plastic: 90}, 350, 280_000, 76)
    Modem3G = MiddleLevelOne("Modem3G", 100, 1120, 1460, {RawMaterialList.Aluminium: 20, RawMaterialList.Copper: 15, RawMaterialList.Plastic: 35}, 90, 90_000, 68)
    PhoneFrame = MiddleLevelOne("PhoneFrame", 272, 910, 1190, {RawMaterialList.Aluminium: 50, RawMaterialList.Plastic: 120, }, 240, 340_000, 102)
    TouchDisplay = MiddleLevelOne("TouchDisplay", 992, 2060, 2670, {RawMaterialList.Silicon: 160, RawMaterialList.Glass: 450, RawMaterialList.Aluminium: 90}, 230, 1_020_000, 291)
