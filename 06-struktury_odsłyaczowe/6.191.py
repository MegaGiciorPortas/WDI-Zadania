"""
Proszę napisać funkcję scalającą dwie posortowane listy w jedną posortowaną listę. Do
funkcji należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wskazanie do
scalonej listy. Zadanie należy wykonać jako funkcję iteracyjną, a następnie jako funkcję rekurencyjną.
"""


class Node:
    def __init__(self, val = 0, next_node = None):
        self.val = val
        self.next = next_node


def intersection(first1, first2):
    dummy = Node(0)
    tail = dummy

    curr1 = first1
    curr2 = first2

    while curr1 is not None and curr2 is not None:
        if curr1.val == curr2.val:
            new_node = Node(curr1.val)
            tail.next = new_node
            tail = new_node
            curr1 = curr1.next
            curr2 = curr2.next
        elif curr1.val < curr2.val:
            curr1 = curr1.next
        else:
            curr2 = curr2.next

    return dummy.next


def new_intersection(first1, first2):
    dummy = Node(0)
    tail = dummy

    cur1 = first1
    cur2 = first2

    while cur1 is not None and cur2 is not None:

        if cur1.val <= cur2.val:
            tail.next = cur1
            tail = tail.next
            cur1 = cur1.next
        else:
            tail.next = cur2
            tail = tail.next
            cur2 = cur2.next

    if cur1 is not None:
        tail.next = cur1
    else:
        tail.next = cur2

    return dummy.next


def merge_recursive(f1, f2, head = None):
    if f1 is None:
        return f2

    if f2 is None:
        return f1

    if f1.val <= f2.val:
        f1.next = merge_recursive(f1.next, f2)
        return f1
    else:
        f2.next = merge_recursive(f1, f2.next)
        return f2
