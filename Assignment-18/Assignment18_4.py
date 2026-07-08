#WAP which accept one number  and return addiion of its factors

def Factors(n):
    Sum = 0
    for i in range(1,n):
        if n % i == 0:
            Sum = Sum + i
    
    return Sum

def main():
    No = int(input("Enter number"))
    Ret = Factors(No)
    print("Addition of factors = ",Ret)

if __name__ == "__main__":
    main()