#Write a lambda function which accepts one number and return cube of that number.

def main():
    No = int(input("Enter a number"))
    Cube = lambda X : X * X * X
    print("Cube of",No,"is",Cube(No))

if __name__ == "__main__":
    main()