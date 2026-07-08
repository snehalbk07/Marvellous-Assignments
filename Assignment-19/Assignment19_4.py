import threading


def compute_sum(numbers, result):
    total = sum(numbers)
    result[0] = total


def compute_product(numbers, result):
    product = 1
    for num in numbers:
        product *= num
    result[1] = product


numbers = list(map(int, input("Enter integers separated by space: ").split()))
result = [0, 1]

thread1 = threading.Thread(target=compute_sum, args=(numbers, result), name="Thread1")
thread2 = threading.Thread(target=compute_product, args=(numbers, result), name="Thread2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Sum of elements:", result[0])
print("Product of elements:", result[1])
