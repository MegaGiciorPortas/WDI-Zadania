"""
Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą
Sita Erastotenesa
"""

from math import isqrt


def func(n):
    if n < 2:
        return

    sito = [1 for _ in range(n)]
    sito[0] = 0
    sito[1] = 0
    licznik = 0

    for i in range(2, isqrt(n) + 1):
        if sito[i]:
            for j in range(i * i, n, i):
                sito[j] = 0

    return sum(sito)


n = int(input("n: "))
print(func(n))
