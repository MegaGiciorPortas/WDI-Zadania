"""
Napisać program wypełniający N-elementową tablicę T liczbami naturalnymi 1-1000 i spraw-
dzający czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.
"""

from random import randint


def func(a):
    flaga = False
    while a > 0:
        c = a % 10
        if c % 2 == 1:
            flaga = True
            break
        a = a // 10
    return flaga

N = int(input("N: "))
T = [randint(1, 1000) for _ in range(N)]

flaga = True
for x in T:
    if not func(x):
        flaga = False
        break

print(flaga)
