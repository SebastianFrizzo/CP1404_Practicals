import string
# total = 0
# count = 0
# sentinel = int(input("Enter age: "))
# while sentinel >= 0:
# 	total += sentinel
# 	count += 1
# 	sentinel = int(input("Enter age: "))
# print(total//count)

# for n in range(0, 5):
# 	print("{:0=2d}".format(n*3))

# errors = True
# while errors:
# 	try:
# 		age = int(input("Enter age: "))
# 		errors = False
# 		if age % 2:
# 			print("Odd")
# 		else:
# 			print("Even")
# 	except ValueError:
# 		print("Not a number")

sentence = "Hello all, how's it going?"
count = 0
# for i, char in enumerate(sentence):
# 	if char.isalpha():
# 		print(i, char)
for char in sentence.lower():
	if char in string.ascii_lowercase:
		count += 1
print(count)



