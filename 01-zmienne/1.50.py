"""
Proszę znaleźć najmniejszą liczbę pierwszą, której suma cyfr wynosi 101, a cyfry są w
porzadku nierosnacym
"""

from math import isqrt


def czy_pierwsza(a):
    if a <= 1:
        return False
    if a <= 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    for i in range(5, isqrt(a) + 1, 2):
        if a % i == 0:
            return False
    return True


def suma_cyfr(a):
    suma = 0
    while a > 0:
        suma += a % 10
        a //= 10
    return suma


def czy_nierosnaca(a):
    a1 = a % 10
    a //= 10

    while a > 0:
        if a % 10 < a1:
            return False
        a1 = a % 10
        a //= 10
    return True


liczba = 999999999776
if liczba % 2 == 0:
    liczba += 1

while liczba <= int(1e20):
    if suma_cyfr(liczba) == 101:
        if czy_nierosnaca(liczba):
            if czy_pierwsza(liczba):
                print(liczba)
                break
    liczba += 2
