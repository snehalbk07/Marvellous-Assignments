#WAP which accept N numbers from user and store it into list.Accept one another number from user & 
#return frequency of that number from list.

def main():
    N = int(input("Enter how many numbers you want to enter"))
    Nos = []

    for i in range(N):
        Ans = int(input("Enter number"))
        Nos.append(Ans)

    Freq = int(input("Enter the number to check frequency in list"))
    Count = 0

    for Ans in Nos:
        if Freq == Ans:
            Count = Count + 1

    print("list =",Nos)
    print("Frequency of",Freq,"number is",Count)

if __name__ == "__main__":
    main()