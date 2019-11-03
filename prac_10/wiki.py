import wikipedia


def main():
	choice = "A"
	while choice != "":
		choice = input("Search Wiki? ")
		try:
			# print(wikipedia.summary(choice, sentences=3))
			wiki_choice = wikipedia.page(choice)
			print(wiki_choice.title)
			print(wiki_choice.url)
			print(wiki_choice.summary)
		except wikipedia.DisambiguationError:
			print("Disambiguation Error")


main()
