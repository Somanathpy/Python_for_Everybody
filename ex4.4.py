#https://books.trinket.io/pfe/05-iterations.html
'''Exercise 2: Write another program that prompts for a list of numbers as above and at the 
end prints out both the maximum and minimum of the numbers instead of the average.'''

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

	