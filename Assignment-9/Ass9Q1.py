#Write a program which acceppts one character and checks whether it is vowel or consonant.

def CheckVowel(Value):
    if(Value =="a" or Value =="e" or Value =="i" or Value =="o" or Value =="u"):
        print("Character is Vowel")
    else:
        print("Character is Consonant")

def main():
    print("Enter a character")
    Text = input()
    CheckVowel(Text)


if __name__ == "__main__":
    main()