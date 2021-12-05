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


def findSums(numbers:list):
	sum_array = []
	first = 0 
	second = 0 
	third = 0
	loop_number = 0

	# You are not detecting when to assign values to variables (first,second,third) and when not to correctly. (If statements)
	# The order in which you check/assign values is incorrect.
	# In other words: you are not telling the computer when to memorize the values and when not to correctly. (It is memorizing when it shouldn't, it is not remembering when it should. And it is calculating/doing things in the wrong order)
	# Draw algorithm/step by step for each loop on paper. Solve the problem by hand, but act like a computer that can only read 1 item at a time and write down every decision/step you make
	for item in numbers:
		loop_number +=1

		if first == 198:
			pass

		first = item


		second = item

		if second == 208:
			pass

		third = item


		summ = first+second+third
		
		
		print('Loop = ', loop_number-1,
			'\t1st = ', first, 
			'\t2nd = ', second,
			'\t3rd = ', third,
			'\tsumm = ', summ,
			'\titem = ', item)


	return sum_array


def main():
	prev_item = 0
	count = 0

	data = getData()
	int_array = intArray(data)


	findSums(int_array)

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