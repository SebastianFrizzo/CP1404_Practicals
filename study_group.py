# total = 0
# count = 0
# sentinel = int(input("Enter age: "))
# while sentinel >= 0:
# 	total += sentinel
# 	count += 1
# 	sentinel = int(input("Enter age: "))
# print(total//count)

# for n in range(0, 5):
# 	print("{:0=2d}".format(n*3))

# errors = True
# while errors:
# 	try:
# 		age = int(input("Enter age: "))
# 		errors = False
# 		if age % 2:
# 			print("Odd")
# 		else:
# 			print("Even")
# 	except ValueError:
# 		print("Not a number")

# import string
# sentence = "Hello all, how's it going?"
# count = 0
# # for i, char in enumerate(sentence):
# # 	if char.isalpha():
# # 		print(i, char)
# for char in sentence.lower():
# 	if char in string.ascii_lowercase:
# 		count += 1
# print(count)


# def is_adult(age):
# 	return age >= 18
#
#
# print(is_adult(17))
# print(is_adult(18))

# products = [["Phone", 320, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
# on_sale = [product for product in products if product[2]]
# cheap_products = [product for product in products if product[1] < 400]
# print(on_sale)
# print(cheap_products)

# class Person:
# 	def __init__(self, name="", age=0):
# 		self.name = name
# 		self.age = age
#
# 	def __str__(self):
# 		return "{} is {} years old".format(self.name, self.age)
#
#
# class Musician(Person):
# 	def __init__(self, name, age, preferred_instrument=""):
# 		super().__init__(name, age)
# 		self.preferred_instrument = preferred_instrument
#
# 	def __str__(self):
# 		return "{} and their preferred instrument is the {}".format(super().__str__(), self.preferred_instrument)
#
#
# class Student(Person):
# 	def __init__(self, name, age, best_subject=""):
# 		super().__init__(name, age)
# 		self.best_subject = best_subject
#
# 	def __str__(self):
# 		return "{} and their best subject is {}".format(super().__str__(), self.best_subject)
#
#
# bobby = Musician("Bobby", 14, "Trumpet")
# steve = Student("Steve", 13, "Maths")
# print(bobby)
# print(steve)

# ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}
# name = input("Enter Name: ")
# age = int(input("Enter Age: "))
# ages_dict[name] = age
# print(ages_dict)
# print(ages_dict["Bill"])
# for key in ages_dict:
# 	print("{}\t-\t{}".format(key, ages_dict[key]))

# read_file = open("study_file.txt", "r")
# state = read_file.read()
# read_file.close()
# write_file = open("study_file.txt", "w")
# if state == "On":
# 	write_file.write("Off")
# 	print("Off")
# else:
# 	write_file.write("On")
# 	print("On")
# write_file.close()

# VOWELS = ["a", "e", "i", "o", "u"]
#
# count = 0
# name = "Bobby McAardvark"
# for letter in name.lower():
# 	if letter in VOWELS:
# 		count += 1
# print("Out of {} letters, {} has {} vowels".format(len(name), name, count))

def get_longest_line(file_name):
	longest_line = ""
	length_longest_line = 0
	index = 0
	read_file = open(file_name, "r")
	for i, line in enumerate(read_file):
		print(line)
		if len(line) > length_longest_line:
			length_longest_line = len(line)
			longest_line = line
			index = i+1
	print(index, longest_line)


get_longest_line("study_file.txt")
