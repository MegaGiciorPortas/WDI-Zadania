"""
Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym wy-
znacza długość najdłuższego, spójnego podciągu arytmetycznego
"""

from random import randint


def func(T):
    wynik = 0
    licznik = 1
    indeks = 0
    r = int(1e6)
    while indeks < len(T) - 1:
        if r == int(1e6):
            r = T[indeks + 1] - T[indeks]
            licznik += 1
            indeks += 1
        else:
            if r == T[indeks + 1] - T[indeks]:
                licznik += 1
                indeks += 1
            else:
                if licznik > wynik:
                    wynik = licznik
                licznik = 1
                r = int(1e6)

    if licznik > wynik:
        return licznik
    return wynik


def func_v2(T):
    if len(T) <= 2:
        return 2
    wynik = 2
    licznik = 2
    r = T[1] - T[0]
    for i in range(2, len(T)):
        if r == T[i] - T[i - 1]:
            licznik += 1
        else:
            if wynik < licznik:
                wynik = licznik
            licznik = 2
            r = T[i] - T[i - 1]

    if licznik > wynik:
        wynik = licznik
    return wynik


N = int(input("N: "))
T = [randint(1, 1000) for _ in range(N)]
print(T)

print(func(T))
