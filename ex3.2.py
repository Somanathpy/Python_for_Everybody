#https://books.trinket.io/pfe/03-conditional.html
'''Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.'''
try:
	hrs = float(input("Enter Hours:"))
	rte = float(input("Enter rate per Hour:"))
	rte = float(rte)
	if hrs >40:
		Pay = (40*rte)+(hrs-40)*(rte * 1.5)
	else:
		Pay = (hrs*rte)
	print("Pay: "+str(Pay))
except:
	print("please enter a number to calculate the temperature")
