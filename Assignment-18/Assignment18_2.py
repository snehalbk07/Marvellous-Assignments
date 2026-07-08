#WAP which accept one number and display pattern

def Display(n):
    i = 0
    while i < n:
        print(" * " * n)
        i = i + 1

def main():
    No = int(input("Enter number"))
    Display(No)

if __name__ == "__main__":
    main()