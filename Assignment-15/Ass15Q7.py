# Write a lambda function using filter() which accepts a list of strings and returns a list of strings 
#having length greater than 5.

GreaterString = lambda X : len(X) > 5

def main():
    strings = ["apple", "banana", "cherry", "date", "elderberry"]
    Ret = list(filter(GreaterString,strings))
    print(Ret)

if __name__ == "__main__":
    main()