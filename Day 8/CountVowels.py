# 4. Write a Python Count vowels in a string.
# Input= “Welcome to Python Assignment”
# Output: Total vowels are: 8.

string = "Welcome to Python Assignment"
count = 0

string = string.lower()

for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':     
        count+=1

if count == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(count))