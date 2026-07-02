#WAP which accepts marks and display grade.
# >=75->distinction
# >=60->first class
# >=50->second class 
# <50->fail


def main():
    Marks = int(input("Enter marks: "))

    if Marks >= 75:
        print("Distinction")
    elif Marks >= 60:   
        print("First class")                        
    elif Marks >= 50:
        print("Second class")       
    else:
        print("Fail")


if __name__ == "__main__":
    main()