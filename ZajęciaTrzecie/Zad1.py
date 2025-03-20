#bez bariery
from threading import Thread
from time import sleep
from random import random

class MyThread(Thread):
    def __init__(self, m):
        Thread.__init__(self)
        self.m = m
    def run(self):
        sleep(random())
        print('Thread', self.m, 'executed A')
        sleep(random())
        print('Thread', self.m, 'executed B')

n_threads = 10
for m in range(n_threads):
    MyThread(m).start()