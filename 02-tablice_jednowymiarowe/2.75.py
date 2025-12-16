"""
Proszę napisać program, który wypełnia N-elementową tablicę T pseudolosowymi liczbami
nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego
znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu arytme-
tycznego o ujemnej różnicy, przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych
indeksach.
"""
from random import randint


def func(T):
    if len(T) < 2:
        return 0

    najdluzszy_dodatni = 1
    najdluzszy_ujemny = 1
    licznik = 2
    r = T[1] - T[0]
    for i in range(2, len(T)):
        if T[i] - T[i - 1] == r:
            licznik += 1
        else:
            if r > 0:
                if licznik > najdluzszy_dodatni:
                    najdluzszy_dodatni = licznik
            elif r < 0:
                if licznik > najdluzszy_ujemny:
                    najdluzszy_ujemny = licznik
            licznik = 2
            r = T[i] - T[i - 1]
    if r > 0:
        if licznik > najdluzszy_dodatni:
            najdluzszy_dodatni = licznik
    elif r < 0:
        if licznik > najdluzszy_ujemny:
            najdluzszy_ujemny = licznik

    return najdluzszy_dodatni - najdluzszy_ujemny


N = int(input("N: "))
T = [2 * randint(0, 49) + 1 for _ in range(N)]

print(func(T))
