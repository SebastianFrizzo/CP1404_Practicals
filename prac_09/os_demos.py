import os


# def main():
# 	"""Demo os module functions."""
# 	print("Starting directory is: {}".format(os.getcwd()))
#
# 	# Change to desired directory
# 	os.chdir('Lyrics/Special')
#
# 	# Print a list of all files in current directory
# 	print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
#
# 	try:
# 		os.mkdir('temp')
# 	except FileExistsError:
# 		pass
#
# 	# Loop through each file in the (current) directory
# 	for filename in os.listdir('.'):
# 		# Ignore directories, just process files
# 		if os.path.isdir(filename):
# 			continue
#
# 		new_name = get_fixed_filename(filename)
#
#
# 	print("Renaming {} to {}".format(filename, new_name))
# 	os.rename(filename, new_name)


def get_fixed_filename(filename):
	"""Return a 'fixed' version of filename."""
	name = ""
	beginning_letter = True
	for count, letter in enumerate(filename):
		if letter.islower():
			beginning_letter = False
			name += letter
		if letter.isupper():
			if beginning_letter:
				name += letter
			else:
				name += " " + letter

	new_name = name.title().replace(" ", "_").replace(".TXT", ".txt")
	return new_name


print(get_fixed_filename("TimeToDuel_da_da_da"))
