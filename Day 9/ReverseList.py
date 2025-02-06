# 5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index.
# Original list: ['red', 'green', 'white', 'black']
# Traverse the said list in reverse order:
# black
# white
# green
# red

color = ["red", "green", "white", "black"]

print("Original list:")
print(color)

print("\nTraverse the said list in reverse order:")

for i in reversed(color):
	print(i)

print("\nTraverse the said list in reverse order with original index:")

for i, el in reversed(list(enumerate(color))):
	print(i, el)