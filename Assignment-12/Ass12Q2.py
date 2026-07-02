#WAP which accepts one number and sum of first N natural numbers

def main():
    No = int(input("Enter number"))

    Sum =0
    for i in range(1,No+1):
        Sum= Sum + i

    print("Sum of first",No,"natural numbers is",Sum)

if __name__ == "__main__":
    main()