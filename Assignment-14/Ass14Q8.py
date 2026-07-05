#Write a lambda function which accepts two numbers and return addition.

Add = lambda a,b : a + b

def main():
    No1 = int(input("Enter first number"))
    No2 = int(input("Enter second number"))
    Ans = Add(No1,No2)
    print("Addition of",No1,"and",No2,"is",Ans)

if __name__ == "__main__":
    main()