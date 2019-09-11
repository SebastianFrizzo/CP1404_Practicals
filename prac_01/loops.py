def main():
	for i in range(1, 21, 2):
		print(i, end=' ')
	print()

	for i in range(0, 101, 10):
		print(i, end=' ')
	print()

	for i in range(20, 0, -1):
		print(i, end=' ')
	print()

	stars = int(input("Please enter a number"))
	for i in range(1, stars + 1):
		print("*", end=' ')
	print()

	for i in range(1, stars + 1):
		print(i * "*", end=' \n')
	print()

	sales = float(input("Enter sales: $"))

	while sales >= 0:
		if sales >= 1000:
			bonus_percentage = 0.15
		elif 0 < sales < 1000:
			bonus_percentage = 0.10
		else:
			bonus_percentage = 0

		bonus = sales * bonus_percentage
		print("{:.2f}".format(bonus))
		sales = float(input("Enter sales: $"))


main()
