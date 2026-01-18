"""
Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do 10 list, według
ostatniej cyfry pola val. W drugim kroku powstałe listy należy połączyć w jedną listę odsyłaczową, która
jest posortowana niemalejąco według ostatniej cyfry pola val.
"""
from random import randint


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def create():
    t = [None] * 10
    return t


def dbg(first):
    while first != None:
        print(first.val, end = ' ')
        first = first.next
    print()


def function(first):
    cur = first
    tablica = create()
    tablica_first = create()

    while cur is not None:
        a = cur.val % 10
        if tablica[a] is None:
            tablica[a] = cur
            tablica_first[a] = cur
        else:
            tablica[a].next = cur
            tablica[a] = cur

        cur = cur.next

    new_first = None
    for i in range(9, -1, -1):
        if tablica[i] != None:
            tablica[i].next = new_first
            new_first = tablica_first[i]

    return new_first


N = randint(10, 30)
first = Node(randint(1, 1000))
cur = first
for i in range(N):
    new_node = Node(randint(1, 1000))
    cur.next = new_node
    cur = new_node

dbg(first)
first = function(first)
dbg(first)
