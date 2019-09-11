from programming_language import ProgrammingLanguage


def main():
	languages = []
	ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
	python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
	visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
	languages.append(ruby)
	languages.append(python)
	languages.append(visual_basic)

	print(language for language in languages)

	print("{}\n{}\n{}".format(ruby, python, visual_basic))

	print("\nThe dynamically typed languages are:")
	for language in languages:
		if language.is_dynamic():
			print(language.name)


main()
