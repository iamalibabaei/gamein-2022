from models.transportation import Transportation, Buss, AirPlane, Ship
from models.products.raw import Product
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


def get_total_price(
        transportation: Transportation, product: Product, number: int, month: int = 1
):
    total_volume = product.volume * number
    return (
            (1 + (0.025 * month))
            * (
                    transportation.get_price(total_volume)
                    + (product.get_max_price() * number)
                    + product.get_variable_price(number)
            )
            // number
    )


def get_price_with_transportation(
        transportation: Transportation, product: Product, number: int
):
    total_volume = product.volume * number
    return (
            transportation.get_price(total_volume)
            + (product.get_max_price() * number)
            + product.get_variable_price(number)
    )


def get_price_with_inventory(
        month: int, transportation: Transportation, product: Product, number: int
):
    return (
            1
            + (0.025 * month)
            * get_price_with_transportation(transportation, product, number)
    ) / number


"""
درصد سود
مجموع سود
هزینه مورد نیاز برای یک ایتریشن
"""


def get_all_data(
        transportation: Transportation, product: Product, number: int, month: int
):
    total_volume = product.volume * number
    per_product_price = (
            (1 + (0.025 * month))
            * (
                    transportation.get_price(total_volume)
                    + (product.get_mean_price() * number)
                    + product.get_variable_price(number)
            )
            // number
    )
    profit_percentage = (((product.min_price + product.max_price) / 2) - per_product_price) / (per_product_price)
    return f"""profit percentage: {profit_percentage}    
total profit: {((((product.min_price + product.max_price) / 2) - per_product_price) * number) // 1_000_000}    
cash flow needed: {(per_product_price * number) // 1_000_000}    
    """


def get_all_data_max(
        transportation: Transportation, product: Product, number: int, month: int
):
    total_volume = product.volume * number
    per_product_price = (
            (1 + (0.025 * month))
            * (
                    transportation.get_price(total_volume)
                    + (product.get_max_price() * number)
                    + product.get_variable_price(number)
            )
            // number
    )
    profit_percentage = (product.max_price - per_product_price) / per_product_price
    return f"""profit percentage: {profit_percentage}    
total profit: {((product.max_price - per_product_price) * number) // 1_000_000}    
cash flow needed: {(per_product_price * number) // 1_000_000}    
    """


def get_all_data_min(
        transportation: Transportation, product: Product, number: int, month: int
):
    total_volume = product.volume * number
    per_product_price = (
            (1 + (0.025 * month))
            * (
                    transportation.get_price(total_volume)
                    + (product.get_min_price() * number)
                    + product.get_variable_price(number)
            )
            // number
    )
    profit_percentage = (product.min_price - per_product_price) / per_product_price
    return f"""profit percentage: {profit_percentage}    
total profit: {((product.min_price - per_product_price) * number) // 1_000_000}    
cash flow needed: {(per_product_price * number) // 1_000_000}    
    """


def get_all_data_mean_max(
        transportation: Transportation, product: Product, number: int, month: int
):
    total_volume = product.volume * number
    per_product_price = (
            (1 + (0.025 * month))
            * (
                    transportation.get_price(total_volume)
                    + (product.get_mean_price() * number)
                    + product.get_variable_price(number)
            )
            // number
    )
    profit_percentage = (product.max_price - per_product_price) / per_product_price
    return profit_percentage, ((product.max_price - per_product_price) * number) // 1_000_000, (
                per_product_price * number) // 1_000_000


def get_all_data_max_mean(
        transportation: Transportation, product: Product, number: int, month: int
):
    total_volume = product.volume * number
    per_product_price = (
            (1 + (0.025 * month))
            * (
                    transportation.get_price(total_volume)
                    + (product.get_max_price() * number)
                    + product.get_variable_price(number)
            )
            // number
    )
    profit_percentage = (product.max_price - per_product_price) / per_product_price
    return profit_percentage, ((product.max_price - per_product_price) * number) // 1_000_000, (
                per_product_price * number) // 1_000_000


def get_all_data_min_max(
        transportation: Transportation, product: Product, number: int, month: int
):
    total_volume = product.volume * number
    per_product_price = (
            (1 + (0.025 * month))
            * (
                    transportation.get_price(total_volume)
                    + (product.get_min_price() * number)
                    + product.get_variable_price(number)
            )
            // number
    )
    profit_percentage = (product.max_price - per_product_price) / per_product_price
    return profit_percentage, ((product.max_price - per_product_price) * number) // 1_000_000, (
                per_product_price * number) // 1_000_000


def get_all_data_max_max(
        transportation: Transportation, product: Product, number: int, month: int
):
    total_volume = product.volume * number
    per_product_price = (
            (1 + (0.025 * month))
            * (
                    transportation.get_price(total_volume)
                    + (product.get_max_price() * number)
                    + product.get_variable_price(number)
            )
            // number
    )
    profit_percentage = (product.max_price - per_product_price) / per_product_price
    return profit_percentage, ((product.max_price - per_product_price) * number) // 1_000_000, (per_product_price * number) // 1_000_000
