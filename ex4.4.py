max = None
min = None
while True:
	number = input("enter a number:")
	if number == 'done':
		print('Done')
		break
	number = int(number)
	if max == None and min == None:
		max = number
		min = number
	elif number > max:
		max = number
	elif number < min:
		min = number
print("Maximum:   "+ str(max)+"     Minimum:   "+str(min))

	