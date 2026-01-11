"""
Proszę zaimplementować zbiór mnogościowy liczb naturalnych korzystając ze struktury listy odsyłaczowej.
• czy element należy do zbioru
• wstawienie elementu do zbioru
• usunięcie elementu ze zbioru
"""
class Node:
    def __init__(self, val = 0, next_node = None):
        self.val = val
        self.next = next_node

# czy wartosc jest w tym zbiorze
def include(first, value):
    curr = first

    while curr is not None:
        if curr.val == value:
            return True
        curr = curr.next
    return False

# dodawanie elementu
def insert(value, first):
    new_node = Node(value)

    if first is None or value < first.val:
        new_node.next = first
        return new_node

    curr = first

    while curr.next is not None and curr.next.val < value:
        curr = curr.next

    if curr.next is not None and curr.next.val == value:
        return first

    new_node.next = curr.next
    curr.next = new_node

    return first

def remove(first, value):
    curr = first

    if first is not None and curr.val == value:
        first = curr.next
        return first

    while curr.next is not None:

        if curr.next.val == value:
            curr.next = curr.next.next
            return first

        if curr.next.val > value:
            return first

        curr = curr.next

    return first