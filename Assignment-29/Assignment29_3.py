# Q3) Display File Line by Line
# Problem Statement:
# WAP which accepts a file name from the user and displays contents of file line by line on screen
# Input:Demo.txt
# Expected Output:
# Display each line of Demo. txt one by one.

import sys

def Display(arg1):
    try:
        dobj = open(arg1,"r")
        Data = dobj.read()

        print("Content of file",arg1,"is\n",Data)

        dobj.close()
    
    except FileNotFoundError as fobj:
        print("file is not present in current directory")

def main():
    Display(sys.argv[1])
    
if __name__ == "__main__":
    main()