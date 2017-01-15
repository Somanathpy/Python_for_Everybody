#https://books.trinket.io/pfe/03-conditional.html
'''Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing 
a message and exiting the program. The following shows two executions of the program:'''
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
