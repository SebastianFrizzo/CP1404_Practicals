def main():
	total_cost = 0
	discount = 0

	number_of_items = int(input("Number of items: "))

	while number_of_items < 0:
		print("Invalid number of items!")
		number_of_items = int(input("Number of items: "))

	if number_of_items > 0:
		for i in range(number_of_items):
			item_cost = float(input("Price of item: "))
			total_cost += item_cost
		if total_cost > 100.00:
			discount = 0.1
		total_cost = total_cost - total_cost * discount
	print("Total price for " + str(number_of_items) + " items is ${:.2f}".format(total_cost))


main()
