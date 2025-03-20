from multiprocessing import RLock
from threading import Thread
from time import sleep
from random import random
from ZajęciaTrzecie.KodZeStrony import Gate

class Barrier:
    def __init__(self, n):
        self.lock = RLock()
        self.gate = Gate()
        self.m = n
    def tryPass(self):
        with self.lock:
            self.m -= 1
            if self.m == 0:
                self.gate.open()
        self.gate.tryPass()


class MyThread(Thread):
    def __init__(self, m):
        Thread.__init__(self)
        self.m = m
    def run(self):
        for i in range(5):
            sleep(random())
            print(f'Thread {self.m} iteration {i} executed A')
            sleep(random())
            print(f'Thread {self.m} iteration {i} executed B')

threads = [MyThread(m) for m in range(10)]
for t in threads:
    t.start()