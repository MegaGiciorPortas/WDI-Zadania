"""
Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca kolejność jej elementów
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def reverse(first):
    if first is None:
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

def show(first,s=""):
    while first is not None:
        s += str(first.val) + " "
        first = first.next
    return s

node = Node(0)
first = node
for i in range(1, 4):
    new_node = Node(i)
    node.next = new_node
    node = new_node

print(show(first))
first = reverse(first)
print(show(first))