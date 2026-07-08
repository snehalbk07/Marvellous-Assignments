# Write a lambda function using map() which accepts a list of numbers and return a list of square of each number.

Square = lambda X: X * X

def main():
    numbers = [1, 2, 3, 4, 5]

    Ret = list(map(Square,numbers))

    print(Ret)  

if __name__ == "__main__":
    main()