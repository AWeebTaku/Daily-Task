#5. Write a lambda function that takes one argument and returns 'Positive' if the number is greater than 0,
#'Negative' if it's less than 0,
# and 'Zero' if it's 0.
# Test it with different numbers.


n = lambda x : "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(2))
print(n(-2))
print(n(0))