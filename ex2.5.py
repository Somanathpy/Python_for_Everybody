#https://books.trinket.io/pfe/02-variables.html
'''Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, 
and print out the converted temperature.'''

Celsius_temperature = float(input("Enter Temperature in Celsius degrees:"))
Fahrenheit_temperature = (Celsius_temperature * 9/5 )+ 32

print("Temperature in Fahrenheit is:" + str(Fahrenheit_temperature))