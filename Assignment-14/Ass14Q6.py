#Write a lambda function which accepts one number and return True if number is odd otherwise False.

Odd = lambda No : True if No % 2 !=0 else False

def main():
    No = int(input("Enter a number"))
    Ans = Odd(No)

    if Ans == True:
        print(No,"is Odd")      
    else:
        print(No,"is Even")
        
if __name__ == "__main__":
    main()