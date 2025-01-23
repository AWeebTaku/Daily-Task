n = int(input("Enter number of lines of pattern: "))

for k in range(1,n+1):
    i = 1
    for i in range(2,k+1):
        print("-",end="")
        
        
    for j in range(i, n+1):
        print(j%2, end="")
    
    print()