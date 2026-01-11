"""
wypisywanie elementów łańcucha
"""


def printing_chain_elements(first):
    curr = first
    while curr is not None:
        print(curr.val)
        curr = curr.next
