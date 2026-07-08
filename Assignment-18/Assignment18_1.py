#Create one module named as Arithmetic which contains 4 functions as Add(),Sub(),Mult() and Div().
#All functions accepts 2 parameters as number and perform the operation.Write py program which 
#call all the functions from Arithmetic module by accepting the parameter from user.

from Arithmetic import *

def main():
    No1 = int(input("Enter first number"))
    No2 = int(input("Enter second number"))

    Add= Addition(No1,No2)
    print("Addition = ",Add)

    Sub= Subtraction(No1,No2)
    print("Subtraction = ",Sub)

    Mult= Multiplication(No1,No2)
    print("Multiplication = ",Mult)

    Div= Division(No1,No2)
    print("Division = ",Div)

if __name__ == "__main__":
    main()