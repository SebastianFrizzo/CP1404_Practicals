""" This program will get 5 numbers from the user, append to a numbers list and process these numbers"""


def main():
	# numbers = []
	# for i in range(0, 5):
	# 	number = int(input("Enter a number: "))
	# 	numbers.append(number)
	#
	# print("The first number is {}".format(numbers[0]))
	# print("The last number is {}".format(numbers[-1]))
	# print("The smallest number is {}".format(min(numbers)))
	# print("The largest number is {}".format(max(numbers)))
	# print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))

	usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
					'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
																												'bob']
	username = input("Enter username: ")
	if username not in usernames:
		print("Access denied")
	else:
		print("Access granted")


main()
