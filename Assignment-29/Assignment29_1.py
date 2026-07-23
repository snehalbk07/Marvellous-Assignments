# Q1) Count Lines in a File
# WAP which accepts a file name from the user and counts how many lines are present in the file.
# input:Demo. txt
# Expected Output:
# Total number of lines in Demo. txt

import sys

def CountLines(arg1):
    try:
        dobj = open(arg1,"r")
        Data = dobj.read()

        Ans = len(Data.splitlines())
        # Ans = len(dobj.readlines())
        print("Total number of lines = ",Ans)

        dobj.close()
    
    except FileNotFoundError as fobj:
        print("file is not present in current directory")

def main():

    CountLines(sys.argv[1])
    

if __name__ == "__main__":
    main()
