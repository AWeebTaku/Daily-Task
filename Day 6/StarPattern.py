n = int(input("Enter number of lines of pattern: "))

for k in range(1,n+1):
	for i in range(k,n):
		print("-",end="")
		i+=1

	for j in range(1,k+1):
		print("*",end="")
		j+=1

	print("\n",end="")

# print("\n")


# for k in range(1,n+1):
# 	for i in range(1,k+1):
# 		print("-",end="")
# 		i+=1

# 	for j in range(i,n+1):
# 		print("*",end="")
# 		j+=1

# 	print("\n",end="")