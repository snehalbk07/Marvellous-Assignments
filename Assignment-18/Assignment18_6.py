#WAP to display pattern

def Display(n):
    for i in range(n, 0, -1):
        print(" * " * i)

def main():
    No = int(input("Enter number"))
    Display(No)

if __name__ == "__main__":
    main()