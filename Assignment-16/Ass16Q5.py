#WAP which accept N numbers from user and store it into list.Return addition of all prime numbers from that list.
#Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our
#user defined module named as MarvellousNum.Name of the function from main python file should be ListPrime().

import MarvellousNum

def ListPrime(X):
    sum = 0

    for no in X:
        if MarvellousNum.ChkPrime(no):
            sum = sum + no

    return sum

def main():
    N = int(input("Enter how many numbers you want to enter"))
    Nos = []

    for i in range(N):
        Ans = int(input("Enter number"))
        Nos.append(Ans)

    Result = ListPrime(Nos)
    print("Addition of prime numbers is:", Result)


if __name__ == "__main__":
    main()