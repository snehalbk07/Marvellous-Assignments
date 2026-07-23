# Q3) Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file named Demo. txt, 
#and copies all contents from the given file into Demo. txt.
# Input (Command Line):
# ABC.txt
# Expected Output:
# Create Demo. txt and copy contents of ABC. txt into Demo. txt.

import sys

def main():

    try:
        robj = open(sys.argv[1],"r")
        Data = robj.read()

        dobj = open("Demo.txt","w")
        dobj.write(Data)

        print("Created Demo.txt and copy contents of ABC.txt into Demo.txt.")


    except FileNotFoundError as fobj:
        print("File is not exists")


if __name__ == "__main__":
    main()