# 3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.
# Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
# Output: UpperCase : 5 LowerCase : 18 NumberCase : 5 SpecialCase : 11

def count_chars(str):
	upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
	
	for i in range(len(str)):
		if str[i] >= 'A' and str[i] <= 'Z':
			upper_ctr += 1
		elif str[i] >= 'a' and str[i] <= 'z':
			lower_ctr += 1
		elif str[i] >= '0' and str[i] <= '9':
			number_ctr += 1
		else:
			special_ctr += 1
		return upper_ctr, lower_ctr, number_ctr, special_ctr

str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
print("Original Substrings:",str)
u, l, n, s = count_chars(str)
print('\nUpper case characters: ',u)
print('Lower case characters: ',l)
print('Number case: ',n)
print('Special case characters: ',s)