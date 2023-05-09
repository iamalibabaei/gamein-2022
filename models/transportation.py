import math


class Transportation:
    def __init__(self, constant, variable):
        self.constant = constant
        self.variable = variable

    def get_price(self, volume):
        return self.constant + (self.variable * math.sqrt(volume))


class Buss(Transportation):
    def __init__(self):
        super().__init__(70_000, 0)


class Ship(Transportation):
    def __init__(self):
        super().__init__(70_000, 100)


class AirPlane(Transportation):
    def __init__(self):
        super().__init__(300_000, 500)
