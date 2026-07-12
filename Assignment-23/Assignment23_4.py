from multiprocessing import Pool
import os
import time

# Function to calculate sum of fifth powers
def sum_of_fifth_powers(n):
    total = sum(i ** 5 for i in range(1, n + 1))
    return (os.getpid(), n, total)

if __name__ == "__main__":
    data = [1000000, 2000000, 3000000, 4000000]

    start_time = time.time()

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(sum_of_fifth_powers, data)

    end_time = time.time()

    # Display results
    for pid, number, total in results:
        print(f"Process ID : {pid}")
        print(f"Input Number : {number}")
        print(f"Sum of Fifth Powers : {total}")
        print("-" * 40)

    print(f"Total Execution Time : {end_time - start_time:.4f} seconds")