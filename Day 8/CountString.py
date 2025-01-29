# 1. Write a Python program to Count all letters, digits, and special symbols from the given string.
# Input = “P@#yn26at^&i5ve”
# Output: Chars = 8 Digits = 2 Symbol = 3

import string

def find_digits_chars_symbols(a):
	letters = sum((ch in string.ascii_lowercase+string.ascii_uppercase) for ch in a)
	digits = sum((ch in string.digits) for ch in a)
	symbols = sum((ch in string.punctuation) for ch in a)
	print("Letters=",letters)
	print("Digits=",digits)
	print("Symbols=",symbols)

find_digits_chars_symbols("P@#yn26at^&i5ve")