from multiprocessing import Pool
import os

# Function to count prime numbers from 1 to n
def count_primes(n):
    count = 0

    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

    return (os.getpid(), n, count)

if __name__ == "__main__":
    data = [10000, 20000, 30000, 40000]

    # Create a pool of worker processes
    with Pool() as pool:
        results = pool.map(count_primes, data)

    # Display results
    for pid, number, count in results:
        print(f"Process ID : {pid}")
        print(f"Input Number : {number}")
        print(f"Total Prime Count : {count}")
        print("-" * 40)