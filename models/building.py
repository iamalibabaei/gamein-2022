class Building:
    def __init__(self, price, capacity, upgrade_price):
        self.price = price
        self.capacity = capacity
        self.upgrade_price = upgrade_price


class Production(Building):
    def __init__(self):
        super().__init__(175_000_000, 2, 130_000_000)


class Assembly(Building):
    def __init__(self):
        super().__init__(185_000_000, 3, 160_000_000)


class Recycle(Building):
    def __init__(self):
        super().__init__(105_000_000, 1, 55_000_000)


class Inventory(Building):
    def __init__(self):
        super().__init__(0, 20_000_000, 645_000_000)
