from models.building import Inventory
from models.transportation import Transportation
from models.products.raw import Product


def calculate_profit(first_price, second_price):
    return round((first_price - second_price) / second_price, 2)


def get_price_with_transportation(
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


def get_price_with_inventory(
        transportation: Transportation,
        product: Product,
        number: int,
        month: int = 1,
        distance: int = 1,
):
    return (
            (1 + (Inventory.VARIABLE * month))
            * get_price_with_transportation(transportation, product, number, distance)
    ) // number


def calculate_profit(first_price, second_price):
    return (first_price - second_price) / second_price


"""
درصد سود
مجموع سود
هزینه مورد نیاز برای یک ایتریشن
"""


def get_all_data(
        transportation: Transportation,
        product: Product,
        number: int,
        month: int
):
    per_product_price = get_price_with_inventory(transportation, product, number, month)
    return f"""profit percentage: {calculate_profit(product.mean_price, per_product_price)}    
total profit: {((product.mean_price - per_product_price) * number) // 1_000_000}    
cash flow needed: {(per_product_price * number) // 1_000_000}    
    """


def get_all_data_max(
        transportation: Transportation, product: Product, number: int, month: int
):
    total_volume = product.volume * number
    per_product_price = (
            (1 + (Inventory.VARIABLE * month))
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
            (1 + (Inventory.VARIABLE * month))
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
            (1 + (Inventory.VARIABLE * month))
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
            (1 + (Inventory.VARIABLE * month))
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
            (1 + (Inventory.VARIABLE * month))
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
            (1 + (Inventory.VARIABLE * month))
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
