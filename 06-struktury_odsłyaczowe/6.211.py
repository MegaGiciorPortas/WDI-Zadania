"""
Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę
elementów w cyklu.
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
            break

    counter = 1
    turtle = turtle.next
    while turtle is not hare:
        counter += 1
        turtle = turtle.next

    return counter
