#zmienne warunowe
from asyncio import Condition
from multiprocessing import RLock


class Gate:
    def __init__(self, is_open = False):
        self.cond = Condition()
        self.is_open = is_open
    #otwieranie bramiki
    def open(self):
        with self.cond:
            self.is_open = True
            self.cond.notify_all()
    #zamyaknie barmki
    def close(self):
        with self.cond:
            self.is_open = False
    def tryPass(self):
        with self.cond:
            self.cond.wait_for(lambda:self.is_open)

