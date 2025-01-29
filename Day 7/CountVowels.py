#4. Write a Python program to count and display the vowels of a given text String=”Welcome to python Training”

string = "Welcome to python Training"
count = 0

string = string.lower()

for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':     
        count+=1

if count == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(count))