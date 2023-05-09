class Building:
    def __init__(self, price, capacity, upgrade_price):
        self.price = price
        self.capacity = capacity
        self.upgrade_price = upgrade_price


class Production(Building):
    def __init__(self):
        super().__init__(285_000_000, 2, 250_000_000)


class Assembly(Building):
    def __init__(self):
        super().__init__(285_000_000, 3, 250_000_000)


class Recycle(Building):
    def __init__(self):
        super().__init__(170_000_000, 3, 86_000_000)


class Inventory(Building):
    def __init__(self):
        super().__init__(0, 5_000_000, 480_000_000)
