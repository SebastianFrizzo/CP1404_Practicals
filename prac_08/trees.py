"""
CP1404/CP5632 Practical
Tree class with inherited (specialised tree) classes
by Trevor Andersen
"""
import random

MAX_WIDTH_OF_TREE = 3


class Tree:
	"""Represent a tree, with trunk height and a number of leaves."""

	def __init__(self):
		"""Initialise a Tree with trunk_height of 1 and full row of leaves."""
		self._trunk_height = 1
		self._leaves = MAX_WIDTH_OF_TREE

	def __str__(self):
		"""Return a string representation of the full Tree, e.g.
		 ###
		 ###
		  |
		  |    """
		return self.get_ascii_leaves() + self.get_ascii_trunk()

	def get_ascii_leaves(self):
		"""Return a string representation of the tree's leaves."""
		result = ""
		if self._leaves % MAX_WIDTH_OF_TREE > 0:
			result += "#" * (self._leaves % MAX_WIDTH_OF_TREE)
			result += "\n"
		for i in range(self._leaves // MAX_WIDTH_OF_TREE):
			result += "#" * MAX_WIDTH_OF_TREE
			result += "\n"
		return result

	def get_ascii_trunk(self):
		"""Return a string representation of the tree's trunk."""
		result = ""
		# the _ (underscore) variable is a convention for an unused variable
		for _ in range(self._trunk_height):
			result += " | \n"
		return result

	def grow(self, sunlight, water):
		"""Grow a tree based on the sunlight and water parameters.
		Randomly grow the trunk height by a number between 0 and water.
		Randomly increase the leaves by a number between 0 and sunlight."""
		self._trunk_height += random.randint(0, water)
		self._leaves += random.randint(0, sunlight)


class EvenTree(Tree):
	def grow(self, sunlight, water):
		"""Grow like a normal tree, but fill out each row of leaves."""
		Tree.grow(self, sunlight, water)
		while self._leaves % 3 != 0:
			self._leaves += 1


class UpsideDownTree(Tree):
	def __str__(self):
		"""Return a string representation of the full tree,
		upside-down compared to a normal tree."""
		return self.get_ascii_trunk() + self.get_ascii_leaves()


class WideTree(Tree):
	def __str__(self):
		return self.get_ascii_leaves() + self.get_ascii_trunk()

	def get_ascii_leaves(self):
		result = ""
		if self._leaves % MAX_WIDTH_OF_TREE > 0:
			result += "##" * (self._leaves % MAX_WIDTH_OF_TREE)
			result += "\n"
		for i in range(self._leaves // MAX_WIDTH_OF_TREE):
			result += "##" * MAX_WIDTH_OF_TREE
			result += "\n"
		return result

	def get_ascii_trunk(self):
		"""Return a string representation of the tree's trunk."""
		result = ""
		# the _ (underscore) variable is a convention for an unused variable
		for _ in range(self._trunk_height):
			result += " || \n"
		return result


class QuickTree(Tree):
	def grow(self, sunlight, water):
		"""Grow a tree based on the sunlight and water parameters.
		Randomly grow the trunk height by a number between 0 and water.
		Randomly increase the leaves by a number between 0 and sunlight."""
		self._trunk_height += water
		self._leaves += sunlight


class FruitTree(Tree):
	def __init__(self):
		super().__init__()
		self._fruit = 1

	def grow(self, sunlight, water):
		super().grow(sunlight, water)
		fruit_grow = random.randint(1, 2)
		fruit_decay = random.randint(1, 5)
		if fruit_grow == 1:
			self._fruit += 1
		if fruit_decay == 1:
			self._fruit -= 1

	def get_ascii_fruit(self):
		result = ""
		print(result)
		if self._fruit <= MAX_WIDTH_OF_TREE:
			result += "." * self._fruit
			result += "\n"
		else:
			self._fruit = MAX_WIDTH_OF_TREE
			result += "." * self._fruit
			result += "\n"
		return result

	def __str__(self):
		return self.get_ascii_fruit() + super().__str__()


class PineTree(Tree):
	def get_ascii_leaves(self):
		result = ""
		if self._leaves % MAX_WIDTH_OF_TREE > 0:
			result += "#" * (self._leaves % MAX_WIDTH_OF_TREE)
			result += "\n"
		for i in range(self._leaves // MAX_WIDTH_OF_TREE):
			result += "#" * MAX_WIDTH_OF_TREE
			result += "\n"
		return result
