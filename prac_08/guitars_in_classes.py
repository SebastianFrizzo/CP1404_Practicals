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
        print(guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    in_file.close()


main()
