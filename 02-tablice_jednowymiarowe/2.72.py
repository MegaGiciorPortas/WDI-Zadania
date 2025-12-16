"""
Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym wy-
znacza długość najdłuższego, spójnego podciągu rosnącego.
"""

from random import randint


def func(T):
    wynik = 0
    licznik = 1
    for i in range(len(T) - 1):
        if T[i] <= T[i + 1]:
            licznik += 1
        else:
            if licznik > wynik:
                wynik = licznik
            licznik = 1
    if licznik > wynik:
        return licznik
    return wynik


N = int(input("N: "))
T = [randint(1, 1000) for _ in range(N)]
print(T)

print(func(T))

