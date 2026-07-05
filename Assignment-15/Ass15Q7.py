# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.


def main():
    strings = ["apple", "banana", "cherry", "date", "elderberry"]
    long_strings = list(filter(lambda x: len(x) > 5, strings))
    print(long_strings)

if __name__ == "__main__":
    main()