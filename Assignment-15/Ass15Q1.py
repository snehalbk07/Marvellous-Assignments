# Write a lambda function using map() which accepts a list of numbers and return a list of square of each number.


def main():
    numbers = [1, 2, 3, 4, 5]
    squares = list(map(lambda x: x ** 2, numbers))
    print(squares)  

if __name__ == "__main__":
    main()