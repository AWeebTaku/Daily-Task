#1. Python program to check leap year

year = int(input("Enter a Year: "))

if year%4 == 0:
	print("It is a Leap Year")
else:
	print("Not a Leap Year")