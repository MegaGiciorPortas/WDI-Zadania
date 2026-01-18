"""
Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać funkcję dodającą
dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def odwracanie_listy(first):
    if first.next is None:
        return first

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


def main_function(first1, first2):
    if first1 is None:
        return first2
    if first2 is None:
        return first1

    first1 = odwracanie_listy(first1)
    cur1 = first1
    first2 = odwracanie_listy(first2)
    cur2 = first2

    dummy = Node(float('inf'))
    last = dummy
    carry = 0

    while cur1 is not None and cur2 is not None:
        liczba = cur1.val + cur2.val + carry
        carry = 0
        if liczba >= 10:
            liczba = liczba % 10
            carry = 1
        new_node = Node(liczba)
        last.next = new_node
        last = new_node

        cur1 = cur1.next
        cur2 = cur2.next

    while cur1 is not None:
        liczba = cur1.val + carry
        carry = 0
        if liczba >= 10:
            liczba = liczba % 10
            carry = 1
        new_node = Node(liczba)
        last.next = new_node
        last = new_node
        cur1 = cur1.next

    while cur2 is not None:
        liczba = cur2.val + carry
        carry = 0
        if liczba >= 10:
            liczba = liczba % 10
            carry = 1
        new_node = Node(liczba)
        last.next = new_node
        last = new_node
        cur2 = cur2.next

    if carry == 1:
        new_node = Node(1)
        last.next = new_node
        last = new_node

    new_first = dummy.next
    new_first = odwracanie_listy(new_first)
    return new_first

    # if cur1 is None:
    #     last.next = cur2
    # if cur2 is None:
    #     last.next = cur1
    #
    # new_first = dummy.next
    # cur = new_first
    #
    # while cur is not None:
    #     if cur.val >= 10:
    #         cur.val = cur.val % 10
    #         if cur.next is None:
    #             new_node = Node(1)
    #             cur.next = new_node
    #             break
    #         else:
    #             cur = cur.next
    #             cur.val = cur.val + 1
    #     else:
    #         cur = cur.next
    #
    # new_first = odwracanie_listy(new_first)
    # return new_first
