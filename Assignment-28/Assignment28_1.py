# Q1) Check File Exists in Current Directory
# Problem Statement:
# write a program which accepts a file name from the user and checks whether that file exists in the current directory or not
#Expected input - Demo.txt
# Expected Output:
# Display whether Demo. txt exists or not.

import os
import sys

def main():
    Ret = os.path.exists(sys.argv[1])

    if(Ret == True):
        print("File exists in current directory")
    else:
        print("File does not exists in current directory")

if __name__ == "__main__":
    main()

