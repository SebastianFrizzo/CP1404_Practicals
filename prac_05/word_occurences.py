user_strings = input("Say something: ").replace(",", "").split(" ")
user_dictionary = {}
max_word_length = 0

for word in user_strings:
	if word not in user_dictionary:
		user_dictionary[word] = 1
		if len(word) > max_word_length:
			max_word_length = len(word)
	else:
		user_dictionary[word] += 1

for word in user_dictionary:
	print("{:{}}: {}".format(word, max_word_length, user_dictionary[word]))
