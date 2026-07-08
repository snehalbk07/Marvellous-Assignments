#WAP which accept N numbers from user and store it into list.Return min number from that list.

def main():
    N = int(input("Enter how many numbers you want to enter"))
    Nos = []

    for i in range(N):
        Ans = int(input("Enter number"))
        Nos.append(Ans)

    Min = Nos[0]
    for Ans in Nos:
        if Ans < Min:
            Min = Ans

    print("List=",Nos)
    print("Minimum number=",Min)

if __name__ == "__main__":
    main()