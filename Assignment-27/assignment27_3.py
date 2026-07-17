# 3: Write a Python program to implement a class named Numbers with the following specifications:
# * The class should contain one instance variable:
# Value
# Define a constructor (init ) that accepts a number from the user and initializes Value.
# * Implement the following instance methods:
# ChkPrime () - returns True if the number is prime, otherwise returns False
# * ChkPerfect () - returns True if the number is perfect, otherwise returns False
# Factors () - displays all factors of the number
# SumFactors () - returns the sum of all factors
# Create multiple objects and call all methods.

class Numbers:

    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False

        return True

    def ChkPerfect(self):
        total = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i

        return total == self.Value

    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total += i

        return total

obj1 = Numbers()

if obj1.ChkPrime():
    print("Prime Number")
else:
    print("Not a Prime Number")

if obj1.ChkPerfect():
    print("Perfect Number")
else:
    print("Not a Perfect Number")

obj1.Factors()
print("Sum of Factors =", obj1.SumFactors())


