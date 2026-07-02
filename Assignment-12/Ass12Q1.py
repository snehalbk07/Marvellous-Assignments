#WAP which accepts one number and prints multiplication table of that number.

def main():
    No = int(input("Enter number"))

    for i in range(1,11,1):
        print(No *i)

if __name__ == "__main__":
    main()