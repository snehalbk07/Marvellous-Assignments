#WAP which accepts one number and check whether it is palindrome or not.

def main():
    No = int(input("Enter a number: "))
    rev = 0
    temp = No
    while No != 0:
        rev = rev * 10 + No % 10
        No = No // 10
    if temp == rev:
        print(temp, "is a palindrome number.")
    else:
        print(temp, "is not a palindrome number.")


if __name__ == "__main__":
    main()
