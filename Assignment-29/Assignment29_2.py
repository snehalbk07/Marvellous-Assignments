# (2) Count Words in a File
# Problem Statement:
# WAP which accepts a file name from the user and counts the total number of words in that file.
# Input:
# Demo.txt
# Expected Output:
# Total number of words in Demo.txt.

import sys

def CountWords(arg1):
    try:
        dobj = open(arg1,"r")
        Data = dobj.read()

        Words = Data.split()
        # Ans = len(dobj.readlines())
        print("Total number of words = ",len(Words))

        dobj.close()
    
    except FileNotFoundError as fobj:
        print("file is not present in current directory")

def main():
    CountWords(sys.argv[1])
    
if __name__ == "__main__":
    main()