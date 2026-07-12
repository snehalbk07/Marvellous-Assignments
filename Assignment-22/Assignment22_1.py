from multiprocessing import Pool
import os

def sum_even_numbers(n):
    # Largest even number <= n
    last_even = n if n % 2 == 0 else n - 1

    # Number of even numbers
    k = last_even // 2

    # Sum of even numbers = 2 + 4 + ... + last_even
    total = k * (k + 1)

    return (os.getpid(), n, total)

if __name__ == "__main__":
    data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as pool:
        results = pool.map(sum_even_numbers, data)

    for pid, number, total in results:
        print(f"Process ID : {pid}")
        print(f"Input Number: {number}")
        print(f"Sum of Even Numbers : {total}")
        print("-" * 40)