from functools import reduce

# Input list of numbers
numbers = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

# Filter numbers between 70 and 90 inclusive
filtered_numbers = list(filter(lambda x: 70 <= x <= 90, numbers))

# Increase each number by 10
mapped_numbers = list(map(lambda x: x + 10, filtered_numbers))

# Multiply all numbers using reduce
product = reduce(lambda x, y: x * y, mapped_numbers)

print("Input List =", numbers)
print("List after filter =", filtered_numbers)
print("List after map =", mapped_numbers)
print("Output of reduce =", product)
