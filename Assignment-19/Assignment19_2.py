import threading


def find_max(numbers):
    maximum = max(numbers)
    print("Maximum element:", maximum)


def find_min(numbers):
    minimum = min(numbers)
    print("Minimum element:", minimum)


numbers = list(map(int, input("Enter integers separated by space: ").split()))

thread1 = threading.Thread(target=find_max, args=(numbers,), name="Thread1")
thread2 = threading.Thread(target=find_min, args=(numbers,), name="Thread2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()
