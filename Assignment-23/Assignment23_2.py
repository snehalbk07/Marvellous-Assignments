from multiprocessing import Pool
import math
import os

# Function to calculate factorial
def factorial(n):
    return (os.getpid(), n, math.factorial(n))

if __name__ == "__main__":
    data = [10, 15, 20, 25]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(factorial, data)

    # Display results
    for pid, number, fact in results:
        print(f"Process ID : {pid}")
        print(f"Input Number : {number}")
        print(f"Factorial : {fact}")
        print("-" * 40)