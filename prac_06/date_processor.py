from date import Date


def main():
    day = int(input("Enter day: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    date = Date(day, month, year)

    choice = "A"
    while choice != "N":
        choice = input("Add days? Y/N: ").upper()
        if choice == "Y":
            additional_days = int(input("How many days have passed?: "))
            date.add_days(additional_days)
        print(date)


main()
