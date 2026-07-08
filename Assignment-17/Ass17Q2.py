#WAP which contains one function named as "ChkNum" which accept one parameter as number.
#If number is even then it should display "Even number" else display "Odd number" on console.

def ChkNum(Number):
    if(Number % 2 == 0):
        print("Even number")
    else:
        print("Odd Number")

def main():
    No = int(input("Enter number"))
    ChkNum(No)

if __name__ == "__main__":
    main()