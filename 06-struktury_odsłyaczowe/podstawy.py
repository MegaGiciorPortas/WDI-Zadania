class Node:
    def __init__(self, val = 0, next_node = None):
        self.val = val
        self.next = next_node


def init():
    return None


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


# usuwanie elementu po wartosci
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


# moc zbioru
def cardinality(first):
    curr = first
    counter = 0

    while curr is not None:
        counter += 1
        curr = curr.next

    return counter


# czy pusty
def empty(first):
    return first is None


# czyszczenie calego zbioru
def clear(first):
    return None


# czesc wspolna
def union(first1, first2):
    dummy = Node(0)
    tail = dummy

    curr1 = first1
    curr2 = first2

    while curr1 is not None and curr2 is not None:

        if curr1.val < curr2.val:
            new_node = Node(curr1.val)
            tail.next = new_node
            tail = new_node
            curr1 = curr1.next
        if curr1.val > curr2.val:
            new_node = Node(curr2.val)
            tail.next = new_node
            tail = new_node
            curr2 = curr2.next
        else:
            new_node = Node(curr1.val)
            tail.next = new_node
            tail = new_node
            curr1 = curr1.next
            curr2 = curr2.next

    while curr1 is not None:
        new_node = Node(curr1.val)
        tail.next = new_node
        tail = new_node
        curr1 = curr1.next

    while curr2 is not None:
        new_node = Node(curr2.val)
        tail.next = new_node
        tail = new_node
        curr2 = curr2.next

    return dummy.next

# czesc wspolna zbiorow
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

# podzbiór (B⊂A)
def subset(firstSup, firstInf):
    currS = firstSup
    currI = firstInf

    while currI is not None and currS is not None:
        if currS.val == currI.val:
            currI = currI.next
            currS = currS.next
        else:
            if currS.val > currI.val:
                return False
            currS = currS.next

    return currI is None

# różnica zbiorów (A\B)
def complement_of_set(firstA, firstB):
    currA = firstA
    currB = firstB

    dummy = Node(0)
    tail = dummy

    while currA is not None and currB is not None:
        if currA.val == currB.val:
            currA = currA.next
            currB = currB.next
        elif currA.val > currB.val:
            currB = currB.next
        else:
            new_node = Node(currA.val)
            tail.next = new_node
            tail = new_node
            currA = currA.next

    while currA is not None:
        new_node = Node(currA.val)
        tail.next = new_node
        tail = new_node
        currA = currA.next

    return dummy.next
