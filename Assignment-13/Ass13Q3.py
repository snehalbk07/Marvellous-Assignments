#WAP which accepts one number and prints sum of digits.

def main():
    No = int(input("Enter a number: "))
    sum = 0
    while No != 0:
        sum = sum + No % 10
        No = No // 10
    print("Sum of digits:", sum)

if __name__ == "__main__":
    main()