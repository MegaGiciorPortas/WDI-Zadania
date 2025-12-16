"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
z nieparzystych cyfr
"""


def czy_same_nieparzyste(n):
    if n == 0:
        return False
    while n > 0:
        last_digit = n % 10
        if last_digit % 2 == 0:
            return False
        n //= 10
    return True


def czy_wiersz_seplnia_warunki(tablica):
    flaga = False
    for liczba in tablica:
        if czy_same_nieparzyste(liczba):
            flaga = True
    return flaga


def main_function(T):
    for wiersz in T:
        if not czy_wiersz_seplnia_warunki(wiersz):
            return False
    return True


T = [
    [10, 22, 135],  # Wiersz 0: Ma '135' -> OK
    [5, 40, 88],  # Wiersz 1: Ma '5' -> OK
    [60, 100, 79]  # Wiersz 2: Ma '79' -> OK
]
T1 = [
    [33, 12, 80],  # Wiersz 0: Ma '33' -> OK
    [40, 7, 100],  # Wiersz 1: Ma '7' -> OK
    [20, 12, 508]  # Wiersz 2: '20', '12', '508' -> BŁĄD
]
T2 = [
    [11, 33, 55],  # Wiersz 0: Ma '11' (lub 33, 55) -> OK
    [1579, 10, 20],  # Wiersz 1: Ma '1579' -> OK
    [130, 552, 798]  # Wiersz 2: '130'(ma 0), '552'(ma 2), '798'(ma 8) -> BŁĄD
]
print(main_function(T))
print(main_function(T1))
print(main_function(T2))
