from multiprocessing import Pool
import os

def count_odd_numbers(n):
    # Count of odd numbers from 1 to n
    count = (n + 1) // 2
    return (os.getpid(), n, count)

if __name__ == "__main__":
    data = [1000000, 2000000, 3000000, 4000000]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(count_odd_numbers, data)

    # Display the results
    for pid, number, count in results:
        print(f"Process ID : {pid}")
        print(f"Input Number : {number}")
        print(f"Odd Number Count : {count}")
        print("-" * 40)