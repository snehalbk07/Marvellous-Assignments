#Write a lambda function which accepts two numbers and return multiplication.

Mult = lambda a,b : a * b

def main():
    No1 = int(input("Enter first number"))
    No2 = int(input("Enter second number"))
    Ans = Mult(No1,No2)
    print("Multiplication of",No1,"and",No2,"is",Ans)

if __name__ == "__main__":
    main()