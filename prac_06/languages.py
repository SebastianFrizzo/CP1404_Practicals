from programming_language import ProgrammingLanguage


def main():
	ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
	python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
	visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
	languages = [ruby, python, visual_basic]

	print("{}\n{}\n{}".format(ruby, python, visual_basic))

	print("\nThe dynamically typed languages are:")
	for language in languages:
		if language.is_dynamic():
			print(language.name)


main()
