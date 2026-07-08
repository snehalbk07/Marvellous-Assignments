import threading


# Event object to synchronize the execution of the threads
start_event = threading.Event()


def thread1():
    for i in range(1, 51):
        print(f"Thread 1: {i}")
    start_event.set()   # Signal that Thread 1 has completed


def thread2():
    start_event.wait()  # Wait until Thread 1 finishes
    for i in range(50, 0, -1):
        print(f"Thread 2: {i}")


if __name__ == "__main__":
    t1 = threading.Thread(target=thread1, name="Thread 1")
    t2 = threading.Thread(target=thread2, name="Thread 2")

    t2.start()
    t1.start()

    t1.join()
    t2.join()
