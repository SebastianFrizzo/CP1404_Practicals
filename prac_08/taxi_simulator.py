from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    current_taxi = None
    choice = None
    prius = Taxi("Prius", 100)
    limo = SilverServiceTaxi("Limo", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 200, 4)

    while choice != "Q":
        choice = input("Let's Drive! \n(Q)uit, (C)hoose taxi, (D)rive \n>>> ").upper()
        if choice == "C":
            print("1 -", prius, "\n2 -", limo, "\n3 -", hummer)
            current_taxi = input("Choose by number\n>>> ")




main()