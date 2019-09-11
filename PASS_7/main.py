from Dog import Dog


def main():
	dog_list = open("Dogs", "r")
	dogs = [dog.strip("\n").split(",") for dog in dog_list]
	print(type(dog in dogs))
	print(dogs)


main()
