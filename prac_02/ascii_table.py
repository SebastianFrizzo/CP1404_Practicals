UPPER_BOUND = 127
LOWER_BOUND = 33


def main():
	user_input = str(input("Enter a character: "))
	# print("The ASCII code for {:<} is {:>}".format(user_input, ord(user_input)))
	print("{:<} {:>}".format(user_input, ord(user_input)))
	user_input = 0
	while LOWER_BOUND > user_input < UPPER_BOUND:
		user_input = int(input("Enter a number between {} and {}: ".format(LOWER_BOUND, UPPER_BOUND)))
	# print("The character for {:<} is {:>}".format(user_input, chr(user_input)))
	print("{:<} {:>}".format(user_input, chr(user_input)))


main()
