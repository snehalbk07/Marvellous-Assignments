import threading


def print_even():
    for num in range(2, 21, 2):
        print(f"Even: {num}")


def print_odd():
    for num in range(1, 20, 2):
        print(f"Odd: {num}")


if __name__ == "__main__":
    even_thread = threading.Thread(target=print_even, name="Even")
    odd_thread = threading.Thread(target=print_odd, name="Odd")

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Both threads completed.")
