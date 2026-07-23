# Q5) Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and 
# returns the frequency (count of occurrences) of that string in the file.
# Input:Demo. txt Marvellous
# Expected Output:
# Count how many times "Marvellous" appears in Demo. txt.

import sys

def main():
    try:
        dobj = open(sys.argv[1],"r")
        Data = dobj.read()

        Count = Data.count(sys.argv[2])
        print("Count of string",sys.argv[2],"is",Count)

        dobj.close()


    except FileNotFoundError as fobj:
        print("File is not exists")


if __name__ == "__main__":
    main()