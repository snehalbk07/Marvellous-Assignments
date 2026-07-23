# Q5) Search a Word in File
# Problem Statement:
# WAP which accepts a file name and a word from the user and checks whether that word is present in file or not
# Input:Demo. txt Marvellous
# Expected Output:
# Display whether the word Marvellous is found in Demo. txt or not.


import sys

def SearchWord(fileName,word):
    try:
        aobj = open(fileName,"r")
        Data = aobj.read()

        if word in Data:
            print("Word is present")
        else:
            print("Word is not present")

        aobj.close()
    
    except FileNotFoundError as fobj:
        print("file is not present in current directory")

def main():
    SearchWord(sys.argv[1],sys.argv[2])
    
if __name__ == "__main__":
    main()
