#WAP to display pattern

def Display(no):
    for i in range(1, no + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def main():
    No = int(input("Enter number"))
    Display(No)

if __name__ == "__main__":
    main()