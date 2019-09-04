COLOUR_DICTIONARY = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Black": "#000000", "BlanchedAlmond": "#ffebcd",
					"BlueViolet": "#8a2be2", "Chocolate": "#d2691e", "DarkGoldenrod": "#b8860b",
					"DarkOrchid": "#9932cc", "DarkSalmon": "#e9967a", "White": "#ffffff"}

colour = input("Enter colour: ")
while colour != "":
	if colour in COLOUR_DICTIONARY:
		print(colour, "is", COLOUR_DICTIONARY[colour])
	else:
		print("Invalid colour")
	colour = input("Enter colour: ")
