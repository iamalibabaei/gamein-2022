from models.building import Inventory
from models.transportation import Transportation
from models.products.raw import Product


def get_max_price_with_transportation(
        transportation: Transportation,
        product: Product,
        number: int,
        distance: int = 1,
):
    total_volume = product.volume * number
    return (
            transportation.get_price(total_volume, distance)
            + (product.get_max_price() * number)
            + product.get_variable_price(number)
    )


def get_max_price_with_inventory(
        transportation: Transportation,
        product: Product,
        number: int,
        month: int = 1,
        distance: int = 1,
):
    return (
            (1 + (Inventory.VARIABLE * month))
            * get_max_price_with_transportation(transportation, product, number, distance)
    ) // number
