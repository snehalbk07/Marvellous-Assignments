#Write a program which accepts one number and check whether it is divisible by 3 and 5.

def Checknumber():
    No = int(input("Enter a number"))
    if(No % 3 == 0 and No % 5 == 0):
        print(No,"is divisible by 3 and 5")
    else:
        print(No,"is not divisible by 3 and 5")

if __name__ == "__main__":
    Checknumber()
