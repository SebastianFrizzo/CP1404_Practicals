from person import Person


def main():
    people = []
    choice = "A"
    while choice != "N":
        choice = input("Add new person to list?: ").upper()
        if choice == "Y":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            age = input("Enter age: ")
            person = Person(first_name, last_name, age)
            people.append(person)
    for person in people:   # todo sort into a table based on ages
        print("{} {} is {} years old.".format(person.first_name, person.last_name, person.age))


main()
