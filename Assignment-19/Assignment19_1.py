import threading


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def display_primes(numbers):
    primes = [num for num in numbers if is_prime(num)]
    print("Prime numbers:", primes)


def display_non_primes(numbers):
    non_primes = [num for num in numbers if not is_prime(num)]
    print("Non-prime numbers:", non_primes)


numbers = list(map(int, input("Enter integers separated by space: ").split()))

thread1 = threading.Thread(target=display_primes, args=(numbers,), name="Prime")
thread2 = threading.Thread(target=display_non_primes, args=(numbers,), name="NonPrime")

thread1.start()
thread2.start()

thread1.join()
thread2.join()
