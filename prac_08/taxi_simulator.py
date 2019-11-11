from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    current_taxi = None
    choice = None
    total_fare = 0
    total_distance_driven = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4),
                 SilverServiceTaxi("Bentley", 150, 6)]
    while choice != "Q":
        choice = input("Let's Drive! \n(Q)uit, (C)hoose taxi, (D)rive \n>>> ").upper()
        if choice == "C":
            print("0 - {}\n1 - {}\n2 - {}\n3 - {}".format(taxis[0], taxis[1], taxis[2], taxis[3]))
            current_taxi = int(input("Choose by number\n>>> "))
        elif choice == "D" and current_taxi is not None:
            trip_distance = int(input("How far will your trip be?: "))
            taxis[current_taxi].drive(trip_distance)
            total_fare += float(taxis[current_taxi].get_fare())
            print("Your trip in the {} cost ${}".format(taxis[current_taxi].name,
                                                        taxis[current_taxi].get_fare()))
            taxis[current_taxi].start_fare()
            total_distance_driven += taxis[current_taxi].trip_meter
            if current_taxi > len(taxis):
                print("Invalid choice")
        elif choice == "D":
            print("Choose a taxi first!")
        print("Current bill = ${:.2f}".format(total_fare))
    print("Taxis are now \n{}\n{}\n{}\n{}".format(taxis[0], taxis[1], taxis[2], taxis[3]))
    print("You travelled {}km with a final fare of ${:.2f}".format(total_distance_driven, total_fare))


main()
