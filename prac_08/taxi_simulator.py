from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    current_taxi = None
    choice = None
    total_fare = 0
    total_distance_driven = 0
    prius = Taxi("Prius", 100)
    limo = SilverServiceTaxi("Limo", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    bentley = SilverServiceTaxi("Bentley", 150, 6)
    taxi_list = [prius, limo, hummer, bentley]

    while choice != "Q":
        choice = input("Let's Drive! \n(Q)uit, (C)hoose taxi, (D)rive \n>>> ").upper()
        if choice == "C":
            print("0 -", prius, "\n1 -", limo, "\n2 -", hummer, "\n3 -", bentley)
            current_taxi = int(input("Choose by number\n>>> "))
        elif choice == "D" and current_taxi is not None:
            trip_distance = int(input("How far will your trip be?: "))
            taxi_list[current_taxi].drive(trip_distance)
            total_fare += float(taxi_list[current_taxi].get_fare())
            print("Your trip in the {} cost ${}".format(taxi_list[current_taxi].name,
                                                        taxi_list[current_taxi].get_fare()))
            taxi_list[current_taxi].start_fare()
            total_distance_driven += taxi_list[current_taxi].trip_meter
            if current_taxi > len(taxi_list):
                print("Invalid choice")
        elif choice == "D":
            print("Choose a taxi first!")
        print("Current bill = ${:.2f}".format(total_fare))
    print("Taxis are now \n{}\n{}\n{}\n{}".format(prius, limo, hummer, bentley))
    print("You travelled {}km with a final fare of ${:.2f}".format(total_distance_driven, total_fare))


main()
