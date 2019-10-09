class Pet:
	def __init__(self, name='', age=0.0, diet='', micro_chipped=False, colour=''):
		self.name = name
		self.age = age
		self.diet = diet
		self.micro_chipped = micro_chipped
		self.colour = colour

	def __str__(self):
		return "The {}, {} is {} years old and has a {} diet".format(self.__class__, self.name, self.age, self.diet)

	def micro_chip_pet(self):
		if self.micro_chipped:
			return "I am micro-chipped!"
		else:
			self.micro_chipped = True
			return "I wasn't, but now am micro-chipped"

	def feed_pet(self):
		if self.diet == "Carnivore":
			return "You feed {} some meat".format(self.name)
		elif self.diet == "Herbivore":
			return "You feed {} some veg".format(self.name)
		elif self.diet == "Omnivore":
			return "You feed {} a balanced meal".format(self.name)
		else:
			return "You feed {} their special food".format(self.name)


class Dog(Pet):
	def __init__(self, name='', age=0.0, diet='Omnivore', micro_chipped=False, colour=''):
		super().__init__(name, age, diet, micro_chipped, colour)

	def bark(self):
		return "Woof!"


class Bulldog(Dog):
	def __init__(self, name='', age=0.0, diet='', micro_chipped=False, colour='', breathing_problem=True):
		super().__init__(name, age, diet, micro_chipped, colour)
		self.breathing_problem = breathing_problem

	def __str__(self):
		return "{} and breathing problems = {}".format(super().__str__(), self.breathing_problem)


class Bird(Pet):
	def __init__(self, name='', age=0.0, diet='', micro_chipped=False, colour=''):
		super().__init__(name, age, diet, micro_chipped, colour)

	def chirp(self):
		return "Whiwhoo"


class Cat(Pet):
	def __init__(self, name='', age=0.0, diet='', micro_chipped=False, colour=''):
		super().__init__(name, age, diet, micro_chipped, colour)

	def meow(self):
		return "Weeooww"


# def tests():
# 	fido = Bulldog("Fido", 4.5, "Medical")
# 	aspen = Cat("Aspen", 0.9, "Carnivore", True, "Champagne")
# 	print(fido)
# 	print(aspen)
# 	print(fido.bark())
# 	print(aspen.meow())
# 	print(fido.micro_chip_pet())
# 	print(aspen.micro_chip_pet())
# 	print(fido.feed_pet())
#
#
# tests()
