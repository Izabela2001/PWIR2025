from threading import Thread, RLock
from time import sleep
from random import random

counter = 0

lock = RLock()

def count(n: int) -> None:
    global counter
    sleep(random())
    with lock:
        print(f"thread {n} enters")
        buf = counter + 1
        if random() < 0.3: raise Exception("Example")
        sleep(0.1*random())
        counter = buf
        print(f"thread {n} leaves")


threads = [Thread(target=count, args=(i,)) for i in range(20)]
for t in threads: t.start()
for t in threads: t.join()
print(f'Threads finished, counter={counter}')