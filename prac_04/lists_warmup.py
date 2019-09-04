def main():
	numbers = [3, 1, 4, 1, 5, 9, 2]
# [0] = 3
# [-1] = 2
# [3] = 1
# [:-1] = 3, 2 /// Wrong, displays as a list from position 1 up to position -1 in normal order
# [3:4] = 1, 5 /// Wrong, doesn't display at the position it ends
# 5 in numbers = 9 /// Wrong, just displays whether it is true that something at this position
# 7 in numbers = IndexError 9 /// Wrong, just displays whether it is true that something at this position
# "3" in numbers = [0] 9 /// Wrong, just displays whether it is true that something at this position
# numbers = [6, 5, 3] =  [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# 	print(numbers[0])
# 	print(numbers[-1])
# 	print(numbers[3])
# 	print(numbers[:-1])
# 	print(numbers[3:4])
# 	print(5 in numbers)
# 	print(7 in numbers)
# 	print("3" in numbers)
# 	print(numbers + [6, 5, 3])
	numbers[0] = 10
	numbers[-1] = 1
	print(numbers[2:])
	for number in numbers:
		if number == 9:
			print("Yes 9 is an element")


main()
