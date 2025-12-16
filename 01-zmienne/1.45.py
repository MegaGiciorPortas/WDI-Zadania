"""
Liczbę pierwszą będącą palindromem nazywamy “palindromem pierwszym”. Liczbę nazy-
wamy “super palindromem pierwszym” jeżeli podczas odrzucania parami skrajnych cyfr do końca pozo-
staje ona palindromem pierwszym. Na przykład, liczba 373929373 jest super palindromem pierwszym bo
373929373, 7392937, 39293, 929, 2 są palindromami pierwszy- mi. Początkowymi super palindromami pierw-
szymi są: 2, 3, 5, 7, 11, 131, 151. Proszę napisać program, który wylicza ile jest super palindromów pierwszych
mniejszych od zadanej liczby n.
"""

from math import isqrt


def czy_palindrom(n):
    return n == n[::-1]


def czy_pierwsza(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    return True


def skracanie_liczby(napis):
    return napis[1:-1]


n = int(input("n: "))
licznik = 0

if n >= 2:
    licznik += 1

for i in range(3, n, 2):
    if czy_pierwsza(i) and czy_palindrom(str(i)):
        flaga = True
        temp = skracanie_liczby(str(i))
        while temp != "":
            if czy_palindrom(temp) and czy_pierwsza(int(temp)):
                temp = skracanie_liczby(temp)
            else:
                flaga = False
                break
        if flaga:
            licznik += 1

print(licznik)
