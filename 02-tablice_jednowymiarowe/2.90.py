"""
Dana jest N-elementowa tablica T, zawierająca liczby. Proszę napisać funkcję, która zwróci
indeks największej liczby, która jest iloczynem wszystkich liczb pierwszych leżących w tablicy na indeksach
mniejszych od niej, lub None jeżeli taka liczba nie istnieje
"""


def czy_pierwsza(n):
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


def czy_istnieje_iloczyn(ciag):
    iloczyn = 1
    N = len(ciag)
    szukana_liczba = ciag[N - 1]

    for i in range(N - 1):
        if czy_pierwsza(ciag[i]):
            iloczyn *= ciag[i]

    if iloczyn == szukana_liczba:
        return szukana_liczba
    return -1


def indeks_najwiekszej_liczby(T):
    najwiekszy_indeks = -1
    najwieksza_liczba = 0

    for i in range(2, len(T) + 1):
        podciag = T[:i]
        iloczyn_podciagu = czy_istnieje_iloczyn(podciag)

        if iloczyn_podciagu > najwieksza_liczba:
            najwiekszy_indeks = i-1
            najwieksza_liczba = iloczyn_podciagu

    if najwiekszy_indeks == -1:
        return None
    return najwiekszy_indeks


T = [2, 3, 6, 2, 5, 60, 3, 180]
T1 = [4, 6, 1, 3, 5, 15]
T2 = [2, 3, 5, 7, 100, 200]
print(indeks_najwiekszej_liczby(T))
print(indeks_najwiekszej_liczby(T1))
print(indeks_najwiekszej_liczby(T2))
