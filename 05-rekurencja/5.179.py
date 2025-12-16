"""
Zadanie 179. Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza
czy jest możliwe pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba kawał-
ków też była liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. Na przykład: divide(2347)=True,
podział na 23 i 47, natomiast divide(2255)=False.
"""

from math import log10


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def zamiana_na_tablice(n):
    dlugosc = int(log10(n)) + 1
    tablica = [0 for _ in range(dlugosc)]
    indeks = dlugosc - 1
    while n > 0:
        tablica[indeks] = n % 10
        n //= 10
        indeks -= 1
    return tablica


def recurension(T, indeks = 0, current = 0, piecies = 0):
    if indeks >= len(T):
        if current == 0:
            return isPrime(piecies)
        if isPrime(current):
            return isPrime(piecies + 1)
        return False

    current = current * 10 + T[indeks]

    if isPrime(current):
        if recurension(T, indeks + 1, 0, piecies + 1):
            return True
    return recurension(T, indeks + 1, current, piecies)

def rekurencja(T, indeks = 0, current = 0, piecies = 0):
    if indeks >= len(T):
        if current == 0:
            return isPrime(piecies)
        if isPrime(current):
            return isPrime(piecies + 1)
        return False

    current = current * 10 + T[indeks]

    if isPrime(current):
        return rekurencja(T,indeks+1, 0, piecies+1) or rekurencja(T, indeks + 1, current, piecies)
    else:
        return rekurencja(T, indeks + 1, current, piecies)


def divide(n):
    tablica = zamiana_na_tablice(n)
    result = recurension(tablica)
    return result

def dzielenie(n):
    tab = zamiana_na_tablice(n)
    result = rekurencja(tab)
    return result

n = int(input("n: "))
print(divide(n))
print(dzielenie(n))

