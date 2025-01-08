#2. Using input function take two number and then swap the number

num1 = int(input("Enter number One:"))
num2 = int(input("Enter number Two:"))
temp1 = 0

print("Number One is:",num1)
print("Number Two is:",num2)

temp1 = num1
num1 = num2
print("Number One is:",num1)

num2 = temp1
print("Number Two is:",temp1)