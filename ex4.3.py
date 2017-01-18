https://books.trinket.io/pfe/04-functions.html
'''Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade 
that takes a score as its parameter and returns a grade as a string.
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
< 0.6    F
~~~
'''
score = input("Enter the score between 0.0 and 1.0:")
#try and catch block to ensure user enters only digits/numbers
try:
	score = float(score) 
except:
	print("please enter a number between 0.0 and 1.0")
	quit()
#initial check to see is not out of range
def computegrade(score):
	if score < 0.0 or score > 1.0:
		return("The entered score is out of range,")
		quit()
	if score >= 0.9:
		return("A")
	elif score >= 0.8:
		return("B")
	elif score >= 0.7:
		return("C")
	elif score >= 0.6:
		return("D")
	elif score < 0.6:
		return("F")

print(computegrade(score))

