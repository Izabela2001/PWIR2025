#
from threading import Thread # umożliwia uruchamianie wielu wątków w tym samym czasie
from queue import SimpleQueue, Empty #umożliwia komunikację między wątkami
from time import sleep #umożlia opóźnienia
from random import random
from typing import NamedTuple #służy do tworzenia nazwanych krotek, które są jak klasy, ale prostsze.

#def klasy danych
#klasa przechowuje dwie zmienne, które będą mnożone
class Query(NamedTuple):
    x: int
    y: int
    #__str__ to metoda, która definiuje, jak ma wyglądać tekstowa reprezentacja obiektu
    def __str__(self) -> str:
        return f"Query: {self.x} * {self.y} = ?"


class Answer(NamedTuple):
    x: int
    y: int
    z: int

    def __str__(self) -> str:
        return f"Answer: {self.x} * {self.y} = {self.z}"

#pusta klasa używana do zakończenia pracy wątków
class Kill(NamedTuple):
    pass

#kolejki
q_query = SimpleQueue() #kolejka, do której będą dodawane zapytania
q_ans = SimpleQueue() #kolejka, w której będą przechowywane odpowiedzi


def client() -> None:
    for x in range(10):
        for y in range(10):
            query = Query(x, y)
            q_query.put(query)
    q_query.put(Kill())


def server() -> None:
    next = True
    while next:
        query = q_query.get()
        match query:
            case Query(x, y):
                q_ans.put(Answer(x, y, x * y))
            case Kill():
                q_ans.put(Kill())
                next = False


def printer() -> None:
    next = True
    while next:
        ans = q_ans.get()
        match ans:
            case Answer():
                print(ans)
            case Kill():
                next = False


threads = (
    Thread(target=client), Thread(target=server), Thread(target=printer)
)

for t in threads: t.start()