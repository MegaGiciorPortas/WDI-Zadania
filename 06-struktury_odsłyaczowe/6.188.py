"""
Zliczanie elementów łańcucha
"""

def cardinality(first):
    curr = first
    counter = 0

    while curr is not None:
        counter += 1
        curr = curr.next

    return counter
