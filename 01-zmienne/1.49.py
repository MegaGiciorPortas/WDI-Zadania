"""
Proszę napisać program wyznaczający najmniejszą liczbę pierwszą o sumie cyfr równej N,
ktorej cyfry sa w porzadku rosnacym
"""
from math import isqrt


def czy_pierwsza(a):
    if a <= 1:
        return False
    if a <= 3:
        return True
    if a % 2 == 0 or a % 3 == 0:
        return False
    i = 5
    while i * i <= a:
        if a % i == 0:
            return False
        i += 2
        if a % i == 0:
            return False
        i += 4
    return True


def czy_rosnaca(a):
    poprzednia = a % 10
    a //= 10
    while a > 0:
        aktualna = a % 10
        a //= 10
        if aktualna >= poprzednia:
            return False
        poprzednia = aktualna
    return True


def suma_cyfr(a, n):
    suma = 0
    while a > 0:
        suma += a % 10
        a //= 10
    if suma == n:
        return True
    return False


n = int(input("n: "))

if n < 2:
    print("Za mala suma!")
elif n == 2:
    print(2)
else:
    liczba = 3
    while True:
        if czy_pierwsza(liczba) and suma_cyfr(liczba, n) and czy_rosnaca(liczba):
            print(liczba)
            break
        liczba += 2
