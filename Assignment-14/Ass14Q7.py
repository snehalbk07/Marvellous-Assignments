#Write a lambda function which accepts one number and return True if divisible by 5.

DivBy5 = lambda No : True if No % 5 ==0 else False

def main():
    No = int(input("Enter a number"))
    Ans = DivBy5(No)
    if Ans == True:
        print(No,"is divisible by 5")   
    else:
        print(No,"is not divisible by 5")

if __name__ == "__main__":
    main()