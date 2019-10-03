from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():   # todo update this to use taxis in a list
    current_taxi = None
    choice = None
    total_fare = 0
    prius = Taxi("Prius", 100)
    limo = SilverServiceTaxi("Limo", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 200, 4)

    while choice != "Q":
        choice = input("Let's Drive! \n(Q)uit, (C)hoose taxi, (D)rive \n>>> ").upper()
        if choice == "C":
            print("1 -", prius, "\n2 -", limo, "\n3 -", hummer)
            current_taxi = int(input("Choose by number\n>>> "))
        elif choice == "D":
            trip_distance = int(input("How far will your trip be?: "))
            if current_taxi == 1:
                prius.drive(trip_distance)
                total_fare += float(prius.get_fare())
                print("Your trip in the {} cost ${}".format(prius.name, prius.get_fare()))
                prius.start_fare()
            elif current_taxi == 2:
                limo.drive(trip_distance)
                total_fare += float(limo.get_fare())
                print("Your trip in the {} cost ${}".format(limo.name, limo.get_fare()))
                limo.start_fare()
            elif current_taxi == 3:
                hummer.drive(trip_distance)
                total_fare += float(hummer.get_fare())
                print("Your trip in the {} cost ${}".format(hummer.name, hummer.get_fare()))
                hummer.start_fare()
            else:
                print("No taxi chosen")
        print("Current bill = ${:.2f}".format(total_fare))
    print("Taxis are now \n{}\n{}\n{}".format(prius, limo, hummer))


main()
