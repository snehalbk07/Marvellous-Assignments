import threading


def even_list(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    even_sum = sum(even_numbers)
    print("Even elements:", even_numbers)
    print("Sum of even elements:", even_sum)


def odd_list(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    odd_sum = sum(odd_numbers)
    print("Odd elements:", odd_numbers)
    print("Sum of odd elements:", odd_sum)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_thread = threading.Thread(target=even_list, args=(numbers,), name="EvenList")
    odd_thread = threading.Thread(target=odd_list, args=(numbers,), name="OddList")

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()
