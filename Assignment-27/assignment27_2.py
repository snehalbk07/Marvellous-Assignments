# 2: Write a Python program to implement a class named BankAccount with the following requirements:
# * The class should contain two instance variables:
# * Name (Account holder name)
# * Amount (Account balance)
# The class should contain one class variable:
# * ROI (Rate of Interest), initialized to 10.5
# Define a constructor (init_) that accepts Name and initial Amount.
# Implement the following instance methods:
# Display () - displays account holder name and current balance
# Deposit () - accepts an amount from the user and adds it to balance
# Withdraw() - accepts an amount from the user and subtracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists)
# CalculateInterest () - calculates and returns interest using formula:
# Interest = (Amount * ROI) / 100
# Create multiple objects and demonstrate all methods.

class BankAccount:

    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter Name:")
        self.Amount = float(input("Enter amount:"))
        

    def Display(self):
        print("Account holder name:",self.Name)
        print("Current balance:",self.Amount)

    def Deposit(self):
        self.Deposit = float(input("Enter deposit amount:"))
        self.Amount = self.Amount + self.Deposit
        print("Balance = ",self.Amount)

    def Withdraw(self):
        self.Withdraw = float(input("Enter withdraw amount:"))
        self.Amount = self.Amount - self.Withdraw
        print("Balance = ",self.Amount)

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest = ",Interest)


obj = BankAccount()
obj.Display()
obj.Deposit()
obj.Withdraw()
obj.CalculateInterest()


