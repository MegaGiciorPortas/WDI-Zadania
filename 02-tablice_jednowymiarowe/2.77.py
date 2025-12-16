"""
Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, że w
grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. Wyznaczyć
wartości prawdopodobieństwa dla N z zakresu 20-40.
"""
from random import randint


def zliczanie_dni(T):
    wyniki = [0 for _ in range(365)]
    for x in T:
        wyniki[x - 1] += 1
        if wyniki[x - 1] > 1:
            return True
    return False


def func(N):
    licznik = 0
    for i in range(10000):
        T = [randint(1, 365) for _ in range(N)]
        if zliczanie_dni(T):
            licznik += 1
    return licznik / 10000


for N in range(20, 41):
    print(f"{N} -> prawdopodobieństwo: {func(N)}")
