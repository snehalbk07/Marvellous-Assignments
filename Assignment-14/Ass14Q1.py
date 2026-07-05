#Write a lambda function which accepts one number and return square of that number.

Square = lambda X : X * X

def main():
    No = int(input("Enter a number"))
    Ans = Square(No)
    print("Square of",No,"is",Ans)

if __name__ == "__main__":
    main()