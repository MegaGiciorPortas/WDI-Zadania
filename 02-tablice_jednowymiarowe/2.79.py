"""
Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. Proszę napisać funkcję zwraca-
jącą wartość typu bool oznaczającą, czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie
jeden element największy (liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej
wartości
"""
from random import randint


def func(T):
    if len(T) == 0:
        return False
    if len(T) == 1:
        return True

    min_el = T[0]
    max_el = T[0]

    for i in range(1, len(T)):
        if T[i] < min_el:
            min_el = T[i]
        elif T[i] > max_el:
            max_el = T[i]

    if max_el == min_el:
        return False

    licznik_min = 0
    licznik_max = 0
    for x in T:
        if x == min_el:
            licznik_min += 1
        elif x == max_el:
            licznik_max += 1
    return licznik_min == 1 == licznik_max


n = int(input("n: "))
T = [randint(1, 100000) for _ in range(n)]

print(func(T))
