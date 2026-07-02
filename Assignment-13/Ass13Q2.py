#WAP which accepts one number and prints count of digits in that number.
def main():
    No = int(input("Enter a number: "))
    count = 0
    while No > 0:
        No = No // 10
        count = count + 1
    print("Count of digits in the number is:", count)  
    

if __name__ == "__main__":
    main()