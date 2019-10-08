from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness=1.2):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return "{}, with a ${:.2f} flag fall and can be rated at {} fanciness".format(super().__str__(), self.flag_fall,
                                                                                      self.fanciness)

    def get_fare(self):
        return "{:.2f}".format(float(super().get_fare()) + self.flag_fall)
