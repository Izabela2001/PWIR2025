from threading import Thread
from queue import SimpleQueue
from typing import NamedTuple


class Query(NamedTuple):
    x: int
    y: int

    def __str__(self) -> str:
        return f"Query: {self.x} * {self.y} = ?"


class Answer(NamedTuple):
    x: int
    y: int
    z: int

    def __str__(self) -> str:
        return f"Answer: {self.x} * {self.y} = {self.z}"


class Kill(NamedTuple):
    pass


q_query = SimpleQueue()
q_ans = SimpleQueue()


def client() -> None:
    for x in range(10):
        for y in range(10):
            query = Query(x, y)
            q_query.put(query)
    q_query.put(Kill())


def server() -> None:
    while True:
        query = q_query.get()
        match query:
            case Query(x, y):
                q_ans.put(Answer(x, y, x * y))
            case Kill():
                q_ans.put(Kill())
                break


def printer() -> None:
    while True:
        ans = q_ans.get()
        match ans:
            case Answer():
                print(ans)
            case Kill():
                break


threads = (
    Thread(target=client), Thread(target=server), Thread(target=printer)
)

for t in threads: t.start()