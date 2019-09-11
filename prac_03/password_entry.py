""" Sebastian."""
"""This program is a simple exercise in input verification."""


def main():
	pass_word = "no"
	verified_pass_word = False
	while not verified_pass_word:
		pass_word = password_entry()
		verified_pass_word = password_verification(pass_word)
	for character in range(len(pass_word)):
		print("*")


def password_entry():
	user_entry = input("Enter a password that is at least 5 characters long and contains upper and lowercase, "
																				"numerical and special characters: ")
	return user_entry


def password_verification(password):
	# upper_verified = 0
	# lower_verified = 0
	# numeric_verified = 0
	# special_verified = 0

	# for character in password:
	# 	if character in password.isupper():
	# 		upper_verified = 1
	# 	if character in password.islower():
	# 		lower_verified = 1
	# 	if character in password.isnumeric():
	# 		numeric_verified = 1
	# 	if character in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]:
	# 		special_verified = 1

	count_lower = 0
	count_upper = 0
	count_digit = 0
	count_special = 0
	for char in password:
		if char.islower():
			count_lower = 1
		if char.isupper():
			count_upper = 1
		if char.isdigit():
			count_digit = 1

	# if upper_verified == 1 and lower_verified == 1 and numeric_verified == 1 and special_verified == 1:
	# 	return True

	if count_lower == 1 and count_upper == 1 and count_digit == 1 and count_special == 1:
		return True


main()
