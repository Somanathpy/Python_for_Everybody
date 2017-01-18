#https://books.trinket.io/pfe/04-functions.html
'''Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay 
which takes two parameters (hours and rate).'''
hours = float(input("enter hours:"))
rate = float(input("enter rate:"))

def computepay(hours,rate):
	#hours = float(input("enter hours:"))
	#rate = float(input("enter rate:"))
	if hours > 40:
		pay = (40*rate)+(hours-40)*(rate*1.5)
	else:
		pay = hours * rate
	return pay
	

print(computepay(hours,rate))