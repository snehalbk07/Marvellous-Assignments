from functools import reduce

# Input list of numbers
numbers = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

# Filter even numbers
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Square each filtered number
mapped_numbers = list(map(lambda x: x * x, filtered_numbers))

# Add all squared numbers using reduce
result = reduce(lambda x, y: x + y, mapped_numbers)

print("Input List =", numbers)
print("List after filter =", filtered_numbers)
print("List after map =", mapped_numbers)
print("Output of reduce =", result)
