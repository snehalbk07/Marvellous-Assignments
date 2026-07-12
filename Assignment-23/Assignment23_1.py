from multiprocessing import Pool
import os

def sum_of_squares(n):
    # Sum of squares from 1 to n
    total = n * (n + 1) * (2 * n + 1) // 6
    return (os.getpid(), n, total)

if __name__ == "__main__":
    data = [1000000, 2000000, 3000000, 4000000]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(sum_of_squares, data)

    # Display the results
    for pid, number, total in results:
        print(f"Process ID : {pid}")
        print(f"Input Number : {number}")
        print(f"Sum of Squares : {total}")
        print("-" * 40)