#2. Declare a square() function with one parameter.
# Then call the function and pass one number and display the square of that number.

def square(n):
	n*=n
	return n

num = int(input("Enter a Number: "))

print("Square of Number is:",square(num))
