#WAP which accepts one number and checks whether it is perfect or not.

def CheckPerfect(N):
    Sum=0
    for i in range(1,N):
        if N % i == 0:
            Sum=Sum + i

    if Sum == N:
        return True
    else:
            return False

def main():
    No = int(input("Enter number"))

    Ret = CheckPerfect(No)
    if Ret == True:
        print(No,"is perfect number")
    else:
        print(No,"is not perfect number")

if __name__ == "__main__":
    main()