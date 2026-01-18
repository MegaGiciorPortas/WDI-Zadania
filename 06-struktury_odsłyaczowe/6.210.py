"""
Dana jestlista, który być może zakończona jest cyklem. Napisać funkcję, która
sprawdza ten fakt
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def algorith_turtle_and_hare(first):
    turtle = first
    hare = first

    while hare is not None and hare.next is not None:
        turtle = turtle.next
        hare = hare.next.next

        if hare == turtle:
            return True

    return False
