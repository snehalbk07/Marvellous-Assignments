#Write a lambda function which accepts three numbers and returns largest number.

Max = lambda a,b,c : a if a>b and a>c else b if b>c else c

def main():
    No1 = int(input("Enter first number"))
    No2 = int(input("Enter second number"))
    No3 = int(input("Enter third number"))

    Ans = Max(No1,No2,No3)
    print("Maximum is",Ans)

if __name__ == "__main__":
    main()