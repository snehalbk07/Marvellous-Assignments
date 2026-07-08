# Write a lambda function using filter() which accepts a list of numbers and return a list of even numbers.

Even = lambda X: X % 2 == 0

def main():
    Nos = [1, 2, 3, 4, 5, 6]
    Ret = list(filter(Even,Nos))

    print(Ret)

if __name__ == "__main__":
    main()