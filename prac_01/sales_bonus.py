"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""


def main():
	sales = float(input("Enter sales: $"))

	if sales >= 1000:
		bonus_percentage = 0.15
	elif 0 < sales < 1000:
		bonus_percentage = 0.10
	else:
		bonus_percentage = 0

	bonus = sales * bonus_percentage
	print("{:.2f}".format(bonus))


main()
