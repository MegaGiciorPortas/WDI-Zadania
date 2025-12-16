"""
Dwie liczby naturalne są 4-zgodne, jeżeli po zapisaniu ich w systemie o podstawie 4, zbiory
cyfr występujące w liczbie są identyczne. Na przykład:
13 = 31(4) i 23 = 113(4)
18 = 102(4) i 33 = 201(4)
107 = 1223(4) i 57 = 321(4).
Dana jest tablica T[N] zawierająca N liczb naturalnych. Proszę napisać funkcję, która zwraca długość naj-
dłuższego podciągu (niekoniecznie spójnego) złożonego z liczb 4-zgodnych
"""


def zamiana_na_system_4(n):
    if n == 0:
        return 0
    wynik = ""
    while n > 0:
        wynik = str(n % 4) + wynik
        n //= 4

    return int(wynik)


def generowanie_liczby_jako_zbior(liczba):
    tablica = [0 for _ in range(4)]
    while liczba > 0:
        tablica[3 - (liczba % 10)] = 1
        liczba //= 10

    wynik = 0
    indeks = 0
    for i in range(len(tablica) - 1, -1, -1):
        if tablica[i] == 1:
            wynik += 2 ** indeks
        indeks += 1
    return wynik


def generowanie_listy_zbiorow(T):
    tablica = [0 for _ in range(len(T))]

    for i in range(len(T)):
        liczba = T[i]
        liczba_w_czworkowym = zamiana_na_system_4(liczba)
        liczba_zbior_przeksztalcona = generowanie_liczby_jako_zbior(liczba_w_czworkowym)

        tablica[i] = liczba_zbior_przeksztalcona

    return tablica


def szukanie_najdluzszego_podciagu(T):
    podciag_maksymlany = 0

    zbiory_liczb = generowanie_listy_zbiorow(T)

    for i in range(len(zbiory_liczb)):
        poczatkowa = zbiory_liczb[i]
        dlugosc = 1
        for j in range(i + 1, len(zbiory_liczb)):
            if zbiory_liczb[j] == poczatkowa:
                dlugosc += 1

        if dlugosc > podciag_maksymlany:
            podciag_maksymlany = dlugosc

    return podciag_maksymlany


T = [13, 50, 33, 23, 48, 18, 15, 34, 24, 8]
print(szukanie_najdluzszego_podciagu(T))
