# Write a lambda function using reduce() which accepts a list of numbers and return maximum element.
from functools import reduce

Max = lambda a,b : a if a>b else b

def main():
    Nos = [1, 2, 3, 4, 5]
    Ret = reduce(Max,Nos)
    
    print(Ret)

if __name__ == "__main__":
    main()