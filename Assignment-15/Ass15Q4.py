# Write a lambda function using reduce() which accepts a list of numbers and return addition of all elements.

from functools import reduce

Addition = lambda a,b : a + b

def main():
    Nos = [1, 2, 3, 4, 5]
    Ret = reduce(Addition, Nos)
    print(Ret)

if __name__ == "__main__":
    main()