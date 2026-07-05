# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.



def main():
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers_count = len(list(filter(lambda x: x % 2 == 0, numbers)))
    print(even_numbers_count)


if __name__ == "__main__":
    main()