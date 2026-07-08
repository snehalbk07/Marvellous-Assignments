import threading


def count_small(text):
    count = sum(1 for ch in text if ch.islower())
    print(f"Thread Name: {threading.current_thread().name}")
    print(f"Thread ID: {threading.get_ident()}")
    print(f"Number of lowercase characters: {count}")


def count_capital(text):
    count = sum(1 for ch in text if ch.isupper())
    print(f"Thread Name: {threading.current_thread().name}")
    print(f"Thread ID: {threading.get_ident()}")
    print(f"Number of uppercase characters: {count}")


def count_digits(text):
    count = sum(1 for ch in text if ch.isdigit())
    print(f"Thread Name: {threading.current_thread().name}")
    print(f"Thread ID: {threading.get_ident()}")
    print(f"Number of digits: {count}")


if __name__ == "__main__":
    text = "Hello123World"

    small_thread = threading.Thread(target=count_small, args=(text,), name="Small")
    capital_thread = threading.Thread(target=count_capital, args=(text,), name="Capital")
    digits_thread = threading.Thread(target=count_digits, args=(text,), name="Digits")

    small_thread.start()
    capital_thread.start()
    digits_thread.start()

    small_thread.join()
    capital_thread.join()
    digits_thread.join()
