#Write a program which accepts radius of circle and prints area of circle.

def CircleArea(r,PI = 3.14):
    Area = PI * r * r
    return Area


def main():

    Radius = float(input("Enter radius"))
    Ret = CircleArea(Radius)
    print("Area of circle :",round(Ret,2))
    

if __name__ == "__main__":
    main()