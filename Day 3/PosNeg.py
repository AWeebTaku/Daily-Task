#3. Python Program to Check if a Number is Positive, Negative or 0

number = int(input("Enter a Number: "))

if number == 0:
	print("Number is Zero")
elif number>0:
	print("Number is Positive")
elif number<0:
	print("Number is Negative")
else:
	print("Invalid Number")