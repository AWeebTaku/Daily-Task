# 2. Write a Python program to remove duplicate characters of a given string.
# Input = “String and String Function”
# Output: String and Function

s1 = "String and String Function"
print("Original String:",s1)
s2 = s1.split()
res = []

for word in s2:
    if word not in res:
        res.append(word)

s3 = ' '.join(res)
print("Corrected String:",s3)