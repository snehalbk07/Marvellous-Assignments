# Q4) Copy File Contents into Another File
# Problem Statement:
# Write a program which accepts two file names from the user.
# * First file is an existing file
# * Second file is a new file
# Copy all contents from the first file into the second file.
# Input:
# ABC.txt Demo.txt
# Expected Output:
# Contents of ABC. txt copied into Demo. txt.

import sys

def CopyContent(a,b):
    try:
        aobj = open(a,"r")
        Data1 = aobj.read()

        bobj = open(b,"a")
        Data2 = bobj.write(Data1)

        print("copied Content =",Data2)

        aobj.close()
        bobj.close()
    
    except FileNotFoundError as fobj:
        print("file is not present in current directory")

def main():
    CopyContent(sys.argv[1],sys.argv[2])
    
if __name__ == "__main__":
    main()