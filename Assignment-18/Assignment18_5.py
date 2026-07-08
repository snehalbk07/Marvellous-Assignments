#WAP which accept one number and check whether number is prime or not

def ChkPrime(no):
    if no <= 1:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True

def main():
    No = int(input("Enter number"))
    Ret = ChkPrime(No)
    
    if(Ret == True):
        print("Prime")
    else:
        print("Not prime")

if __name__ == "__main__":
    main()