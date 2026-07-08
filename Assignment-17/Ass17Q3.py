#WAP which contains one function named as Add() which accepts 2 numbers from user and return addition.

def Add():
    No1 = int(input("Enter first number"))
    No2 = int(input("Enter second number"))

    Ans = No1 + No2
    return Ans

def main():
    Ret = Add()
    print("Addition =",Ret)

if __name__ == "__main__":
    main()