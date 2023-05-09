from enum import Enum

from models.products.raw import Product, RawMaterialList


class MiddleLevelOne(Product):
    def __init__(self, name, volume, min_price, max_price, dependencies={}, production_rate=None, fixed_cost=None, variable_cost=None):
        super().__init__(name, volume, min_price, max_price, dependencies, production_rate, fixed_cost, variable_cost)


class MiddleLevelOneList(Enum):
    Modem2G = MiddleLevelOne("Modem 2G", 80, 1700, 3200, {RawMaterialList.Aluminium: 15, RawMaterialList.Copper: 10, RawMaterialList.Plastic: 30}, 100, 173031, 214)
    DisplayKeypad = MiddleLevelOne("DisplayKeypad", 328, 3300, 5600, {RawMaterialList.Aluminium: 30, RawMaterialList.Glass: 150, RawMaterialList.Silicon: 50}, 80, 243682, 461)
    PhoneBattery = MiddleLevelOne("PhoneBattery", 240, 1600, 2500, {RawMaterialList.Cobalt: 18, RawMaterialList.Lithium: 12, }, 240, 399933, 243)
    PhoneKeypad = MiddleLevelOne("PhoneKeypad", 592, 4700, 7300, {RawMaterialList.Aluminium: 70, RawMaterialList.Plastic: 300}, 80, 404945, 738)
    Camera = MiddleLevelOne("Camera", 224, 2200, 3300, {RawMaterialList.Copper: 20, RawMaterialList.Glass: 40, RawMaterialList.Plastic: 90}, 250, 641719, 336)
    Modem3G = MiddleLevelOne("Modem3G", 100, 2300, 4300, {RawMaterialList.Aluminium: 20, RawMaterialList.Copper: 15, RawMaterialList.Plastic: 35}, 100, 218915, 295)
    PhoneFrame = MiddleLevelOne("PhoneFrame", 272, 2600, 3700, {RawMaterialList.Aluminium: 50, RawMaterialList.Plastic: 120, }, 310 ,1026669, 442)
    TouchDisplay = MiddleLevelOne("TouchDisplay", 992, 8500, 10200, {RawMaterialList.Silicon: 160, RawMaterialList.Glass: 450, RawMaterialList.Aluminium: 90}, 290, 2885592, 1440)
