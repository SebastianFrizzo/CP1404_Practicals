from car import Car


def main():
    print("Let's drive!")
    car_name = input("Enter your car name: ")
    car = Car(car_name)

    choice = "A"
    while choice != "Q":
        print(car)
        choice = input("Menu \n (D)rive \n (R)efuel \n (Q)uit \nEnter your choice: ").upper()
        if choice == "D":
            validated = False
            while not validated:
                distance = input("How many km do you wish to drive?: ")
                validated = validate_number_positive(distance)
            distance = int(distance)
            car.drive(distance)

        elif choice == "R":
            validated = False
            while not validated:
                fuel = input("How many units of fuel do you want to add to the car?: ")
                validated = validate_number_positive(fuel)
            fuel = int(fuel)
            car.add_fuel(fuel)

    print("Goodbye {}'s driver".format(car_name))


def validate_number_positive(number):
    try:
        number = int(number)
        return True
    except ValueError:
        print("Invalid")
        return False


main()
