# user_name = input("What is your name? ")
# names_file = open("names.txt", "w")
# print(user_name, file=names_file)
# names_file.close()
#
# names_file = open("names.txt", "r")
# for line in names_file:
# 	print("Hello {}".format(line))
# names_file.close()
#
# numbers_file = open("numbers.txt", "w")
# print(17, file=numbers_file)
# print(42, file=numbers_file)
# numbers_file.close()
#
# numbers_file = open("numbers.txt", "r")
# total = 0
# for line in numbers_file:
# 	total += int(line)
# print(total)
# numbers_file.close()

numbers_file = open("numbers.txt", "w")
choice = "Y"
while choice == "Y":
	number = input("Please enter a number")
	# print(number, file=numbers_file)
	numbers_file.write(number + "\n")
	choice = input("Would you like to enter another number, Y or N").upper()
	while choice not in ["Y", "N"]:
		choice = input("Would you like to enter another number, Y or N").upper()
numbers_file.close()

numbers_file = open("numbers.txt", "r")
total = 0
for line in numbers_file:
	total += int(line)
print(total)
numbers_file.close()
