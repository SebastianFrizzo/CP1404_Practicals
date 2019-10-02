from prac_06.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return super().__str__()

    def drive(self, distance):
        reliability_check = randint(1, 101)
        if reliability_check < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            print("{} broke down".format(self.name))
            distance_driven = super().drive(0)
            return distance_driven
