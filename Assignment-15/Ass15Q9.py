# Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.

from functools import reduce

Product = lambda a,b : a * b

def main():
    numbers = [1, 2, 3, 4, 5]
    Ret = reduce(Product, numbers)
    print(Ret)

if __name__ == "__main__":
    main()