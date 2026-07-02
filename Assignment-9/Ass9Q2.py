#write a program which accepts one number and prints its factors

def Factors(No):
    for i in range(1, No + 1):
        if(No % i == 0):
            print(i)        

def main():
    No = int(input("Enter Number"))
    Factors(No)

if __name__ == "__main__":
    main()