#WAP which accepts one number and checks whether it is prime or not.

def main():
    No = int(input("Enter a number: "))

    if No % 2 == 0:
        print(No, "is not a prime number.")
    else:
        print(No, "is a prime number.")
    

if __name__ == "__main__":
    main()