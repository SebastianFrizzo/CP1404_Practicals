def repeat_string(word):
	if word.endswith("."):
		return word.capitalize()
	else:
		word += "."
		return word.capitalize()


print(repeat_string("hello. I am confused"))

