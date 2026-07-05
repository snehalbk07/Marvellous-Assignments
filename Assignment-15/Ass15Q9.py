# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.


def main():
    from functools import reduce
    numbers = [1, 2, 3, 4, 5]
    product = reduce(lambda x, y: x * y, numbers)
    print(product)

if __name__ == "__main__":
    main()