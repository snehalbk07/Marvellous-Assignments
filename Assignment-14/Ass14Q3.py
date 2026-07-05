#Write a lambda function which accepts two numbers and return maximun number.

Max= lambda a,b: a if a>b else b

def main():
    No1 = int(input("Enter first number"))
    No2 = int(input("Enter second number"))
    
    Ans = Max(No1,No2)
    print("Maximum of",No1,"and",No2,"is",Ans)

if __name__ == "__main__":
    main()