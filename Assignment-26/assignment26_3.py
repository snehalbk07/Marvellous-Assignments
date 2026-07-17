# 3: Write a Python program to implement a class named Arithmetic with the following characteristics:
# * The class should contain two instance variables: Valuel and Value2.
# * Define a constructor (init) that initializes all instance variables to O.
# * Implement the following instance methods:
# * Accept () - accepts values for Valuel and Value2 from the user.
# * Addition () - returns the addition of Valuel and Value2.
# Subtraction () - returns the subtraction of Valuel and Value2.
# * Multiplication () - returns the multiplication of Valuel and Value2.
# Division () - returns the division of Valuel and Value2 (handle division by zero properly).
# Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter Value1 "))
        self.Value2 = int(input("Enter Value2 "))

    def Addition(self):
        Add = self.Value1 + self.Value2
        print("Addition = ",Add)

    def Subtraction(self):
        Sub = self.Value1 - self.Value2
        print("Subtraction = ",Sub)

    def Multiplication(self):
        Mul = self.Value1 * self.Value2
        print("Multiplication = ",Mul)

    def Division(self):
        try:
            Div = self.Value1 / self.Value2
            print("Division = ",Div)
        except Exception as eobj:
            print("Division = Cannot divide by 0")

obj = Arithmetic()
obj.Accept()
obj.Addition()
obj.Subtraction()
obj.Multiplication()
obj.Division()