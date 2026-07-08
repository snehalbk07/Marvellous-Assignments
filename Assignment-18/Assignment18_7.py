#WAP to display pattern

def Display(no):
    pattern = ""
    
    for i in range(1, no + 1):
        pattern = pattern + str( i )
    
    for i in range(no):
        print(pattern)

def main():
    No = int(input("Enter number"))
    Display(No)

if __name__ == "__main__":
    main()