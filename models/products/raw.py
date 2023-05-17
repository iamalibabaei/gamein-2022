from enum import Enum


class Product:
    def __init__(self, name, volume, min_price, max_price, dependencies={}, production_rate=None, fixed_cost=None,
                 variable_cost=None):
        self.name = name
        self.volume = volume
        self.min_price = min_price
        self.max_price = max_price
        self.dependencies = dependencies
        self.production_rate = production_rate
        self.fixed_cost = fixed_cost
        self.variable_cost = variable_cost

    def get_price(self):
        res = 0
        for key, value in self.dependencies.items():
            if isinstance(key.value, RawMaterial):
                res += key.value.min_price * value
            else:
                res += key.value.get_price() * value
        return res

    def get_price_with_count(self, count):
        return self.get_price() * count

    def get_variable_price(self, total_number):
        return self.fixed_cost + (self.variable_cost * total_number)

    def get_max_price(self):
        res = 0
        for key, value in self.dependencies.items():
            res += key.value.max_price * value
        return res

    def get_mean_price(self):
        res = 0
        for key, value in self.dependencies.items():
            res += ((key.value.max_price + key.value.min_price) / 2) * value
        return res

    def get_min_price(self):
        res = 0
        for key, value in self.dependencies.items():
            res += key.value.min_price * value
        return res

    @property
    def mean_price(self):
        return (self.max_price + self.min_price) // 2


class RawMaterial(Product):
    def __init__(self, name, volume, min_price):
        super().__init__(name, volume, min_price, min_price)


class RawMaterialList(Enum):
    Aluminium = RawMaterial("Aluminium", 2, 4, )
    Chips = RawMaterial("Chips", 30, 100, )
    Cobalt = RawMaterial("Cobalt", 10, 10, )
    Copper = RawMaterial("Copper", 1, 7, )
    Glass = RawMaterial("Glass", 2, 1, )
    Lithium = RawMaterial("Lithium", 10, 2, )
    Microphone = RawMaterial("Microphone", 15, 50, )
    Plastic = RawMaterial("Plastic", 2, 1,)
    Ports = RawMaterial("Ports", 50, 40, )
    Processors = RawMaterial("Processors", 10, 50, )
    Silicon = RawMaterial("Silicon", 1, 1,)
    Speaker = RawMaterial("Speaker", 3, 25)
    VibrationMotor = RawMaterial("VibrationMotor", 50, 150)
