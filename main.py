from typing import List

from models.transportation import Transportation, Buss, AirPlane, Ship
from models.products.raw import RawMaterialList, Product
from models.products.middle_one import MiddleLevelOneList
from models.products.middle_two import MiddleLevelTwoList
from models.products.final import FinalList

buss = Buss()
ship = Ship()
air_plane = AirPlane()

print("MiddleLevelOneList")
for product in MiddleLevelOneList:
    print(product.value.name, product.value.get_max_price())

print("MiddleLevelTwoList")
for product in MiddleLevelTwoList:
    print(product.value.name, product.value.get_max_price())

print("Final")
for product in FinalList:
    print(product.value.name, product.value.get_max_price())


def get_total_price(transportation: Transportation, product: Product, number: int, month: int = 1):
    total_volume = product.volume * number
    return (1 + (0.025 * month)) * (
                transportation.get_price(total_volume) + (product.get_max_price() * number) + product.get_variable_price(number)) // number


def get_price_with_transportation(transportation: Transportation, product: Product, number: int):
    total_volume = product.volume * number
    return (transportation.get_price(total_volume) + (product.get_max_price() * number) + product.get_variable_price(
        number))


def get_price_with_inventory(month: int, transportation: Transportation, product: Product, number: int):
    return (1 + (0.025 * month) * get_price_with_transportation(transportation, product, number)) / number
