#WAP which accept N numbers from user and store it into list.Return max number from that list.
def main():
    N = int(input("Enter how many numbers you want to enter"))
    Nos = []

    for i in range(N):
        Ans = int(input("Enter number"))
        Nos.append(Ans)
    
    Max = Nos[0]
    for Ans in Nos:
        if Ans > Max:
            Max = Ans

    print(Nos)
    print("Maximum number=",Max)


if __name__ == "__main__":
    main()
