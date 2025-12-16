"""
Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym wy-
znacza długość najdłuższego, spójnego podciągu geometrycznego.
"""

from random import randint


def func(T):
    if len(T) <= 2:
        return 2
    wynik = 2
    licznik = 2
    for i in range(2, len(T)):
        a = T[i - 2]
        b = T[i - 1]
        c = T[i]

        if b * b == a * c:
            licznik += 1
        else:
            if licznik > wynik:
                wynik = licznik
            licznik = 2

    if licznik > wynik:
        wynik = licznik
    return wynik


N = int(input("N: "))
T = [randint(1, 1000) for _ in range(N)]
print(T)

print(func(T))
