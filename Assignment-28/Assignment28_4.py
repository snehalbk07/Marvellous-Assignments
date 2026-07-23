# Q4) Compare Two Files (Command Line)
# Problem Statement:
# WAP which accepts two file names through command line arguments and compares the contents of both files
# If both files contain the same contents, display Success
# Otherwise display Failure
# Input (Command Line):
# Demo.txt Hello.txt
# Expected Output:
# Success OR Failure

import sys

def main():

    try:

        aobj = open(sys.argv[1],"r")
        bobj = open(sys.argv[2], "r")

        Data1 = aobj.read()
        Data2 = bobj.read()

        if(Data1 == Data2):
            print("Success")
        else:
            print("Failure")




    except FileNotFoundError as fobj:
        print("File is not exists")


if __name__ == "__main__":
    main()