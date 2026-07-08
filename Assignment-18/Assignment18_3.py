#WAP which accept one number and return its factorial.

def Factorial(no):
    fact = 1

    for i in range(1, no + 1):
        fact = fact * i

    return fact

def main():
    No = int(input("Enter number"))
    Ret = Factorial(No)
    print("Factorial = ",Ret)

if __name__ == "__main__":
    main()