from multiprocessing import Pool
import math
import os

def calculate_factorial(n):
    # Calculate factorial of n
    fact = math.factorial(n)
    return (os.getpid(), n, fact)

if __name__ == "__main__":
    data = [10, 15, 20, 25]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(calculate_factorial, data)

    # Display the results
    for pid, number, fact in results:
        print(f"Process ID : {pid}")
        print(f"Input Number : {number}")
        print(f"Factorial : {fact}")
        print("-" * 40)