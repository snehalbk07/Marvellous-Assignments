#Write a program whcih accepts length and width of rectangle and prints area.
def RectArea(L,W):
    Area = L * W
    return Area

def main():
    Length = int(input("Enter length"))
    Width = int(input("Enter width"))

    Ret = RectArea(Length,Width)
    print("Area of rectangle :",Ret)

if __name__ == "__main__":
    main()