"""
Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne elementy listy przechowują
kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1.
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def odwracanie_listy(first):
    p = None
    q = first
    r = first.next

    while r is not None:
        q.next = p
        p = q
        q = r
        r = r.next

    q.next = p
    return q


def main_function(first):
    new_first = odwracanie_listy(first)
    cur = new_first

    while cur is not None:
        if cur.val <= 8:
            cur.val = cur.val + 1
            break
        else:
            cur.val = 0
            if cur.next is not None:
                cur = cur.next
            else:
                new_node = Node(1)
                cur.next = new_node
                break

    first = odwracanie_listy(new_first)
    return first
