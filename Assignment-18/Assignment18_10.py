#WAP which accept number from user and return addition of digits in that number

def SumDigits(no):
    sum = 0

    while no != 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10

    return sum

def main():
    No = int(input("Enter number"))
    Ret = SumDigits(No)
    print("Addition of digits=",Ret)

if __name__ == "__main__":
    main()