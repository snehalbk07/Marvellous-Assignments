#WAP which accepts one number and print reverse of that number.

def main():
    No = int(input("Enter a number: "))
    rev = 0
    while No != 0:
        rev = rev * 10 + No % 10
        No = No // 10
    print("Reverse of the number is:", rev)


if __name__ == "__main__":
    main()