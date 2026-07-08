#WAP which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false

def Div():
    No = int(input("Enter number"))

    if(No % 5 == 0):
        return True
    else:
        return False

def main():
    Ret = Div()

    if(Ret == True):
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")

if __name__ == "__main__":
    main()