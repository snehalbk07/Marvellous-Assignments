#WAP which accept number from user and check whether that number is positive or negative or 0.

def main():
    No = int(input("Enter number"))

    if(No > 0):
        print("positive number")
    elif(No < 0):
        print("Negative number")
    else:
        print("Zero")

if __name__ == "__main__":
    main()