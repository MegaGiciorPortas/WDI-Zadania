"""
Napisać program wypełniający N-elementową tablicę T liczbami pseudolosowymi z zakresu
1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.
"""

from random import randint
from sys import exit


def czy_same_nieparzyste(n):
    while n > 0:
        cyfra = n % 10
        n = n // 10
        if cyfra % 2 == 0:
            return False
    return True


N = int(input("N: "))
T = [randint(1, 1000) for _ in range(N)]

for x in T:
    if czy_same_nieparzyste(x):
        print("TAK")
        exit(0)

print("NIE")
