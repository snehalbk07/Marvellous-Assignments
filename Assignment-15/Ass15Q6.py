# Write a lambda function using reduce() which accepts a list of numbers and return minimum element.

from functools import reduce

Min = lambda a,b : a if a<b else b

def main():
    Nos = [1, 2, 3, 4, 5]
    Ret = reduce(Min,Nos)
    
    print(Ret)

if __name__ == "__main__":
    main()