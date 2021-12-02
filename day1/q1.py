import os

def getData():
	data = []

	file = open("q1.txt", "r")
	data = file.readlines()
	
	return data


def intArray(array:list):
	result_array = []

	for item in array:
		result_array.append(int(item))

	return result_array


def main():
	prev_item = 0
	count = 0

	data = getData()
	int_array = intArray(data)

	for item in int_array:
		
		
		# if item == 198:
		# 	prev_item = item
		# 	continue

		if item > prev_item:
			count += 1
		prev_item = item

	print(len(int_array))
	print(len(data))

	print(count-1)

main()



