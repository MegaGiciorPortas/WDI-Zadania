"""
Listy odsyłaczowe budowane są z obiektów zawierających dwa pola: val przechowujące liczbę naturalną oraz
pole next przechowujące wskaźnik do kolejnego elementu. Dane były dwie niepuste listy odsyłaczowe rów-
nej długości, każda zawierała rosnący ciąg arytmetyczny zaczynający się od wartości 1. Nieudane scalanie
tych list spowodowało powstanie jednej listy o całkowicie pomieszanej kolejności elementów. Proszę napisać
funkcję fix(p), która z takiej listy odtwarza dwie listy sprzed nieudanego scalania. Do funkcji przekazujemy
wskaźnik na scaloną listę, funkcja powinna zwrócić dwa wskaźniki na odtworzone listy.
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def add(first, inserted):
    inserted.next = None

    if first is None:
        return inserted

    # sprawdzenie czy nie trzeba tej wartosci dac na sam poczatek
    if first.val > inserted.val:
        inserted.next = first
        return inserted

    # jezeli nie to sprawdzamy gdzie go powinnismy dac
    # napoczatku sprawdzamy czy element first jest samemu w lancuchu czy jest wiecej elementow
    if first.next is not None:
        p = None
        q = first

        while q is not None:
            # przypadek kiedy znalezlismy miejsce w ktore wsadzic szuakan wartosc
            if q.val > inserted.val:
                p.next = inserted
                inserted.next = q
                return first
            p = q
            q = q.next
        # przypadek kiedy wartosc insert jest najwieksza
        p.next = inserted
        return first
    # przypadek kiedy nowy lancuch ma narazie tylko jeden element i wartosc insert jest wieksz od wartosci first
    else:
        first.next = inserted
        return first


def fix(first):
    new_first = None  # wskaznik do posortowanego lancucha

    cur = first
    while cur is not None:
        current = cur
        cur = cur.next
        new_first = add(new_first, current)

    f1 = new_first
    c1 = f1
    new_first = new_first.next
    f2 = new_first
    c2 = f2
    new_first = new_first.next

    r = new_first.val - 1

    while new_first is not None:
        next_node = new_first.next
        if new_first.val - c1.val == r:
            c1.next = new_first
            c1 = c1.next
            c1.next = None
        else:
            c2.next = new_first
            c2 = c2.next
            c2.next = None
        new_first = next_node

    return f1, f2
