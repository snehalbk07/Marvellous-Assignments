# Write a lambda function using reduce() which accepts a list of numbers and return minimum element.

def main(): 
    from functools import reduce
    numbers = [1, 2, 3, 4, 5]
    minimum = reduce(lambda x, y: x if x < y else y, numbers)
    print(minimum)


if __name__ == "__main__":
    main()