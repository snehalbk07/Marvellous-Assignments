from functools import reduce


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


numbers = [2, 70, 11, 10, 17, 23, 31, 77]

filtered_numbers = list(filter(is_prime, numbers))
mapped_numbers = list(map(lambda x: x * 2, filtered_numbers))
maximum_number = reduce(lambda x, y: x if x > y else y, mapped_numbers)

print("Input List =", numbers)
print("List after filter =", filtered_numbers)
print("List after map =", mapped_numbers)
print("Output of reduce =", maximum_number)
