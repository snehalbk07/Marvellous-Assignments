# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers 
#divisible by both 3 and 5.

Div = lambda X : X % 3 == 0 and X % 5 == 0

def main():
    Nos = [1, 2, 3, 4, 5, 15, 30, 45, 60]
    Ret = list(filter(Div,Nos))
    print(Ret)

if __name__ == "__main__":
    main()