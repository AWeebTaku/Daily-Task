#2. Write a Python program to get the largest and smallest number from a list without builtin functions.

a = [345,234,5,2345,4,534,234]
smallest = a[0]
largest = a[0]

for val in a:
	if val < smallest:
		smallest = val
	if val > largest:
		largest = val

print("The Smallest Element is",smallest)
print("The Largest Element is",largest)