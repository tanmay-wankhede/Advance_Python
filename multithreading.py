from threading import Thread
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

threads = []
num_threads = 10

for i in range(num_threads):
    t = threads(target=square_numbers)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print('end main')

