from prac_08.guitar import Guitar
import csv
from collections import namedtuple


def main():
    guitars = []
    in_file = open('guitars.csv', 'r', newline='')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)

    choice = "A"
    while choice != "N":
        choice = input("Would you like to add a guitar? Y or N \n>>>").upper()
        if choice == "Y":
            name = input("Enter Guitar name: ")
            year = input("Enter year of production: ")
            price = float(input("Enter price: "))
            guitar = Guitar(name, year, price)
            guitars.append(guitar)

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    out_file = open('my_guitars.csv', 'w')
    for guitar in guitars:
        guitar_parts = [guitar.name, guitar.year, str(guitar.price)]
        guitar_string = ",".join(guitar_parts)
        print(guitar_string, file=out_file)

    out_file.close()
    in_file.close()


main()
