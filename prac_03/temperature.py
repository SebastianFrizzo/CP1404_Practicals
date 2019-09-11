def main():
	choice = "A"
	while choice != "Q":
		display_menu()
		choice = choose_conversion()
		choice_handling(choice)
	print("Thank you.")


def display_menu():
	menu = """C - Convert Celsius to Fahrenheit
	F - Convert Fahrenheit to Celsius
	Q - Quit"""
	print(menu)


def choose_conversion():
	choice = input(">>> ").upper()
	return choice


def choice_handling(choice):
	if choice == "C":
		celsius = float(input("Celsius: "))
		fahrenheit = convert_celsius_to_fahrenheit(celsius)
		print("Result: {:.2f} F".format(fahrenheit))

	elif choice == "F":
		fahrenheit = float(input("Fahrenheit: "))
		celsius = convert_fahrenheit_to_celsius(fahrenheit)
		print("Result: {:.2f} C".format(celsius))

	elif choice != "Q":
		print("Invalid option")


def convert_celsius_to_fahrenheit(celsius):
	fahrenheit = celsius * 9.0 / 5 + 32
	return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
	celsius = (fahrenheit - 32) * 5 / 9
	return celsius


main()
