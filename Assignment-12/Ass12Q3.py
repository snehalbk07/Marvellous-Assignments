#WAP which accepts one number and prints factorial of that number.

def main():
    No = int(input("Enter number"))

    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i

    print("Factorial of",No,"is",Fact)
    
if __name__ == "__main__":
    main()