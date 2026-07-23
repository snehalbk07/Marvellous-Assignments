# Q2) Display File Contents
# Problem Statement:
# console.
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on console
# Input:Demo.txt
# Expected Output:
# Display contents of Demo. txt on console

import sys
import os

def main():
    Ret = os.path.exists(sys.argv[1])

    if(Ret == True):
        fobj = open(sys.argv[1],"r")
        Data = fobj.read()
        print("Display contents of",sys.argv[1],"on console",Data)

    else:
        print("File does not exists")

if __name__ == "__main__":
    main()