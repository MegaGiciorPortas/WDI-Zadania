"""
Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie z liczb
nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego podciągu
lub wartość 0 jeżeli taki podciąg nie istnieje.
"""
from random import randint


def szukanie_wyrazow_nieparzystych(T):
    wyrazy_nieparzyste = [0 for _ in range(len(T))]
    for i in range(len(T)):
        if T[i] % 2 == 1:
            wyrazy_nieparzyste[i] = 1

    return wyrazy_nieparzyste


def szukanie_podciagow_pod_poalindromy(ciag):
    if sprawdzenie_czy_palindrom(ciag):
        return len(ciag)
    for dlugosc in range(len(ciag) - 1, 0, -1):
        for i in range(len(ciag) - dlugosc + 1):
            if sprawdzenie_czy_palindrom(ciag[i:i + dlugosc]):
                return dlugosc
    return 0


def sprawdzenie_czy_palindrom(ciag):
    if len(ciag) == 1:
        return True
    for i in range((len(ciag) + 1) // 2):
        if ciag[i] != ciag[len(ciag) - 1 - i]:
            return False
    return True


def funkcja_main(T):
    wyrazy_nieparzyste = szukanie_wyrazow_nieparzystych(T)

    najdluzszy_palindrom = 0
    dlugosc_ciagu = 0
    for i in range(len(T)):
        if wyrazy_nieparzyste[i] == 1:
            dlugosc_ciagu += 1
        else:
            ciag = T[i - dlugosc_ciagu: i]
            dlugosc_palindromu = szukanie_podciagow_pod_poalindromy(ciag)
            if dlugosc_palindromu > najdluzszy_palindrom:
                najdluzszy_palindrom = dlugosc_palindromu
            dlugosc_ciagu = 0
    if dlugosc_ciagu > najdluzszy_palindrom:
        ciag = T[len(T) - dlugosc_ciagu:len(T)]
        dlugosc_palindromu = szukanie_podciagow_pod_poalindromy(ciag)
        if dlugosc_palindromu > najdluzszy_palindrom:
            najdluzszy_palindrom = dlugosc_palindromu

    return najdluzszy_palindrom

# N = int(input("N: "))
# T = [randint(1, 1000) for _ in range(N)]
# T = [1, 2, 3, 5, 3, 8, 1, 3, 2]
# print(funkcja_main(T))
