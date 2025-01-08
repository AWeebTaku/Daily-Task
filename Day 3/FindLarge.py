num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))
num3 = int(input("Enter number three: "))

if num1<num2 and num2>num3:
	print("Number Two is the Largest:",num2)
elif num2<num1 and num1>num3:
	print("Number One is the Largest:",num1)
elif num3>num1 and num3>num2:
	print("Number Three is the Largest:",num3)
else:
	print("All numbers are equal")