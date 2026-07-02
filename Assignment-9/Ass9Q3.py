#Write a program which accepts two numbers and prints addition, Subtraction, multiplication and division.

def Addition(N1,N2):
    Ans =N1 + N2
    return Ans

def Subtraction(N1,N2):
    Ans =N1 - N2
    return Ans

def Multiplication(N1,N2):
    Ans = N1 * N2
    return Ans

def Division(N1,N2):
    Ans = N1 / N2
    return Ans

def main():
    No1 = int(input("Enter first number"))
    No2 = int(input("Enter second number"))

    Ret1 = Addition(No1,No2)
    print("Addition = ",Ret1)

    Ret2 = Subtraction(No1,No2)
    print("Subtraction = ",Ret2)

    Ret3 = Multiplication(No1,No2)
    print("Multiplication = ",Ret3)

    Ret4 = Division(No1,No2)
    print("Division = ",Ret4)

if __name__ == "__main__":
    main()