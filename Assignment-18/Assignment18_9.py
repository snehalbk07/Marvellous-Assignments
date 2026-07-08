#WAP which accept number from user and return number of digits in that number

def CountDigits(no):
    count = 0

    while no != 0:
        no = no // 10
        count = count + 1

    return count

def main():
    No = int(input("Enter number"))
    Ret = CountDigits(No)
    print("Number of digits=",Ret)

if __name__ == "__main__":
    main()