#Write a lambda function which accepts one number and return True if number is even otherwise False.

Even = lambda No : True if No % 2 ==0 else False

def main():
    No = int(input("Enter a number"))
    Ans = Even(No)
    
    if Ans == True:
        print(No,"is Even") 
    else:
        print(No,"is Odd")
    
if __name__ == "__main__":
    main()