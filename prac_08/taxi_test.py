from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    # car = Taxi("Prius 1", 100)
    # car.drive(40)
    # print(car)
    # print(car.get_fare())
    # car.start_fare()
    # print(car)

    car = SilverServiceTaxi("Bentley", 100, 2)
    car.drive(18)
    print(car)
    print(car.get_fare())
    car.start_fare()
    print(car)


main()
