from prac_08.unreliable_car import UnreliableCar

def main():
    car = UnreliableCar('car_1', 100, 50)
    car.drive(100)
    print(car)

if __name__ == '__main__':
    main()