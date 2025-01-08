#1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd
num1 = int(input("Enter a number: "))
if num1 == 0:
	print("Number is neither even nor odd")
elif num1%2 == 0:
	print("Number is Even")
else:
	print("Number is Odd")