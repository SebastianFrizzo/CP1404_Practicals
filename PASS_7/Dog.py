class Dog:

	def __init__(self, name = "", breed = "", age = 0):
		self.name = name
		self.breed = breed
		self.age = age

	def __str__(self):
		return "{},{},{}".format(self.name, self.breed, self.age)

