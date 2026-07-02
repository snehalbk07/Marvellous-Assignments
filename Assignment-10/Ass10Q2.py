#Write a program which contains one function ChkGreater() that accepts 2 numbers and prints the greater number.


def ChkGreater():
    No1 = int(input("Enter first number"))
    No2 = int(input("Enter second number"))

    if(No1 > No2):
        print("Greater number :", No1)
    else:
        print("Greater number :", No2)

if __name__ == "__main__":
    ChkGreater()