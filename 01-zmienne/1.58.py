"""
Zadanie 58. Liczbę nazywamy iloczynowo-pierwszą jeżeli iloczyn jej cyfr w systemie o podstawie b jest
liczbą pierwszą. Na przykład: 13 jest liczbą iloczynowo-pierwszą w systemie dziesiętnym, bo 1 ∗3 = 3 16 jest
liczbą iloczynowo-pierwszą w systemie trójkowym, bo 16 = 121(3),1 ∗2 ∗1 = 2 W liczbie naturalnej możemy
dokonywać rotacji jej cyfr, np. 1428, 4281, 2814, 8142 albo 209, 092, 920. Proszę napisać funkcję, która dla
danej liczby naturalnej N, zwróci najmniejszą podstawę systemu (z zakresu 2-16) w którym przynajmniej
jedna z rotowanych liczb jest iloczynowo-pierwsza albo wartość None gdy taka podstawa nie istnieje.
"""
from math import log2, ceil, isqrt


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


def zamiana_na_podstawe(n, p):
    if n == 0:
        return "0"
    N = ceil(log2(n)) + 1
    tablica = [0 for _ in range(N)]
    indeks = 0
    while n > 0:
        tablica[indeks] = n % p
        n = n // p
        indeks += 1

    wynik = ""
    for i in range(indeks - 1, -1, -1):
        if tablica[i] >= 10:
            wynik += chr((tablica[i] % 10) + 65)
        else:
            wynik += str(tablica[i])

    return wynik


def iloczyn_liczby(n):
    wynik = 1
    for a in n:
        if 48 <= ord(a) <= 57:
            wynik *= int(a)
        else:
            wynik *= int(ord(a) - 55)
    return wynik


def funkcja(n):
    aktualna_rotacja = n
    for i in range(2, 17):
        for j in range(len(n)):
            if czy_pierwsza(iloczyn_liczby(zamiana_na_podstawe(int(aktualna_rotacja),i))):
                return i
            aktualna_rotacja = aktualna_rotacja[len(aktualna_rotacja) - 1] + aktualna_rotacja[
                0:len(aktualna_rotacja) - 1]
    return None


n = input("n: ")
print(funkcja(n))
