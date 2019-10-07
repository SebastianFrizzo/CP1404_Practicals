from prac_08.guitar import Guitar
import csv
from collections import namedtuple


def main():
    in_file = open('guitars.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)
    reader = csv.reader(in_file)  # use default dialect, Excel

    for row in reader:
        print(row)
        # guitar = Guitar._make(row)
        # print(repr(guitar))
    in_file.close()


main()
