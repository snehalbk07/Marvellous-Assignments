# Write a lambda function using filter() which accepts a list of numbers and return a list of even numbers.


def main():
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)

if __name__ == "__main__":
    main()