#3. Write a Python program to find duplicate values from a list and display those.

a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
s = set()
dup = []

for n in a:
    if n in s:
        dup.append(n)
    else:
        s.add(n)

print("The Duplicate Elements are",dup)