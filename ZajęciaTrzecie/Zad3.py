from threading import Thread, RLock, Event
from time import sleep
from random import random

class Barrier:
    def __init__(self, n):
        self.lock = RLock()
        self.gate = Event()
        self.m = n
        self.gate.clear()
    def tryPass(self):
        with self.lock:
            self.m -= 1
            if self.m == 0:
                self.gate.set()
        self.gate.wait()

class MyThread(Thread):
    def __init__(self, m):
        Thread.__init__(self)
        self.m = m
    def run(self):
        sleep(random())
        print('Thread', self.m, 'executed A')
        barrier.tryPass()
        sleep(random())
        print('Thread', self.m, 'executed B')

n_threads = 10
barrier = Barrier(n_threads)
for m in range(n_threads):
    MyThread(m).start()