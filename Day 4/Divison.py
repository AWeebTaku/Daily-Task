#1. Declare a div() function with two parameters.
# Then call the function and pass two numbers and display their division.

def division(a,b):
	result = a/b
	return result

num1 = int(input("Enter the Dividend: "))
num2 = int(input("Enter the Divisor: "))

print("Quotient:",division(num1,num2))