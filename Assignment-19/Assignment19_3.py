import threading

counter = 0
lock = threading.Lock()


def increment_counter():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1


threads = []
for i in range(5):
    thread = threading.Thread(target=increment_counter, name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Final value of counter:", counter)
