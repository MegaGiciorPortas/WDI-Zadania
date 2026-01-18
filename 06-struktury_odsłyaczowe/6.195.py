"""
Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji należy przekazać wska-
zanie na pierwszy element listy.
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def usuwanie_ostatniego_elementu(first):
    if first is None or first.next is None:
        return None

    cur = first
    last = None
    while cur.next is not None:
        last = cur
        cur = cur.next
    last.next = None
    return first


def dbg(first):
    while first != None:
        print(first.val, end = ' ')
        first = first.next
    print()


