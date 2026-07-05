# Write a lambda function using reduce() which accepts a list of numbers and return addition of all elements.


def main():
    from functools import reduce
    numbers = [1, 2, 3, 4, 5]
    total_sum = reduce(lambda x, y: x + y, numbers)
    print(total_sum)

if __name__ == "__main__":
    main()