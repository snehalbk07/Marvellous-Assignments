from multiprocessing import Pool
import os

def sum_odd_numbers(n):
    # Largest odd number <= n
    last_odd = n if n % 2 != 0 else n - 1

    # Number of odd numbers
    k = (last_odd + 1) // 2

    # Sum of odd numbers = 1 + 3 + ... + last_odd = k^2
    total = k * k

    return (os.getpid(), n, total)

if __name__ == "__main__":
    data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as pool:
        results = pool.map(sum_odd_numbers, data)

    for pid, number, total in results:
        print(f"Process ID : {pid}")
        print(f"Input Number : {number}")
        print(f"Sum of Odd Numbers : {total}")
        print("-" * 40)