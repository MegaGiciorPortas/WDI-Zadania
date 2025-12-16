"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
parzystą
"""


def czy_zawiera_cyfre_parzysta(n):
    if n == 0:
        return True
    while n > 0:
        last_digit = n % 10
        if last_digit % 2 == 0:
            return True
        n //= 10
    return False


def czy_wiersz_seplnia_warunki(tablica):
    for liczba in tablica:
        if not czy_zawiera_cyfre_parzysta(liczba):
            return False
    return True


def main_function(T):
    for wiersz in T:
        if czy_wiersz_seplnia_warunki(wiersz):
            return True
    return False


T1 = [
    [24, 60, 102],  # Wiersz 0: OK, OK, OK  -> TEN WIERSZ PASUJE
    [13, 55, 91],  # Wiersz 1: ZŁA, ZŁA, ZŁA
    [8, 20, 4]  # Wiersz 2: OK, OK, OK  -> TEN TEŻ PASUJE
]
T2 = [
    [22, 46, 135],  # Wiersz 0: OK, OK, ZŁA  -> Wiersz odpada
    [1, 88, 20],  # Wiersz 1: ZŁA, OK, OK  -> Wiersz odpada
    [90, 6, 77]  # Wiersz 2: OK, OK, ZŁA  -> Wiersz odpada
]
T3 = [
    [11, 33, 55],  # Wiersz 0: ZŁA, ZŁA, ZŁA -> Wiersz odpada
    [10, 30, 51],  # Wiersz 1: OK, OK, ZŁA   -> Wiersz odpada
    [8, 100, 204]  # Wiersz 2: OK, OK, OK   -> TEN WIERSZ PASUJE
]
print(main_function(T1))
print(main_function(T2))
print(main_function(T3))
