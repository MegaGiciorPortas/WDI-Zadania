"""
Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. Proszę napisać trzyfunkcje:
• inicjalizującą tablicę,
• zwracającą wartość elementu o indeksie n,
• podstawiającą wartość value pod indeks n.
"""


class Node:
    def __init__(self, value, indeks, next_node = None):
        self.val = value
        self.idx = indeks
        self.next = next_node


def init_array():
    return None


def wartosc(first, indeks):
    curr = first

    while curr is not None:
        if curr.idx == indeks:
            return curr.val
        if curr.idx > indeks:
            return 0
        curr = curr.next

    return 0


def indeks(first, indeks, value):
    curr = first

    if curr is None or curr.idx > indeks:
        new_node = Node(value, indeks)
        new_node.next = first
        return new_node

    if curr.idx == indeks:
        curr.val = value
        return first

    while curr.next is not None:

        if curr.next.idx == indeks:
            curr.next.val = value
            return first

        if curr.next.idx > indeks:
            new_node = Node(value, indeks)
            new_node.next = curr.next
            curr.next = new_node
            return first

        curr = curr.next

    new_node = Node(value, indeks)
    curr.next = new_node


    return first
