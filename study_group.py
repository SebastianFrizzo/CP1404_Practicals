# import string
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

ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}
name = input("Enter Name: ")
age = int(input("Enter Age: "))
ages_dict[name] = age
print(ages_dict)
print(ages_dict["Bill"])
for key in ages_dict:
	print("{}\t-\t{}".format(key, ages_dict[key]))
