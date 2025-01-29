#1. Write a Python program to count the occurrences of each word in a given sentence string = “To change the overall look of your document. To change the look available in the gallery” 

str = "To change the overall look your document. To change the look available in the gallery"
print(str)

while len(str) > 0:
	x = input("Enter the String for Counting(Type exit to leave): ")
	if x == "exit":
		break
	
	print(str.count(x))




# c = dict()

# txt = str.split(" ")

# for t in txt:
# 	if t in c:
# 		c[t] += 1
# 	else:
# 		c[t] = 1

# print(c,"\n")