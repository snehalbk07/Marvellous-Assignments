#WAP which accept N numbers from user and store it into list.Return addition of all elements from that list.

def main():
    N = int(input("Enter how many numbers you want to enter"))
    Nos = []
    Sum = 0

    for i in range(N):
        Ans = int(input("Enter number"))
        Sum = Sum + Ans
        Nos.append(Ans)
    print(Nos)
    print("Addition of all elements=",Sum)

if __name__ == "__main__":
    main()