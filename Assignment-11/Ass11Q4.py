#WAP which accepts one number and prints binary equivalent.

def DecimalToBinary(No):
    Binary = 0
    i = 1
    while No != 0:
        Rem = No % 2
        Binary = Binary + (Rem * i)
        No = No // 2
        i = i * 10

    return Binary


def main():
    No = int(input("Enter number: "))
    Ret = DecimalToBinary(No)
    print("Binary equivalent of", No, "is", Ret)


if __name__ == "__main__":
    main()