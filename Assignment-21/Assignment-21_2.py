import threading


def even_factors(number):
    factors = [i for i in range(1, number + 1) if number % i == 0 and i % 2 == 0]
    total = sum(factors)
    print(f"Even factors of {number}: {factors}")
    print(f"Sum of even factors: {total}")


def odd_factors(number):
    factors = [i for i in range(1, number + 1) if number % i == 0 and i % 2 != 0]
    total = sum(factors)
    print(f"Odd factors of {number}: {factors}")
    print(f"Sum of odd factors: {total}")


if __name__ == "__main__":
    number = int(input("Enter a number: "))

    even_thread = threading.Thread(target=even_factors, args=(number,), name="EvenFactor")
    odd_thread = threading.Thread(target=odd_factors, args=(number,), name="OddFactor")

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Exit from main")
