# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

def main():
    numbers = [1, 2, 3, 4, 5, 15, 30, 45, 60]
    divisible_by_3_and_5 = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers))
    print(divisible_by_3_and_5)

if __name__ == "__main__":
    main()