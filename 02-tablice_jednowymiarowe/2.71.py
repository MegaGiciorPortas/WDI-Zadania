"""
Dana jest N-elementowa tablica T zawierająca liczby naturalne. W tablicy możemy prze-
skoczyć z pola o indeksie k o npól w prawo jeżeli wartość njest czynnikiem pierwszym liczby T[k]. Napisać
funkcję sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole
"""
from random import randint


def rozklad_na_czynniki(n):
    tablica = []
    czynnik = 2
    while czynnik * czynnik <= n:
        if n % czynnik == 0:
            tablica.append(czynnik)
            while n % czynnik == 0:
                n = n // czynnik
        else:
            czynnik += 1
    if n > 1:
        tablica.append(n)
    return tablica


def czy_da_sie(T, S, i):
    if i == len(T) - 1:
        return True
    if S[i] == 1:
        return False

    S[i] = 1

    czynniki = rozklad_na_czynniki(T[i])
    for czynnik in czynniki:
        if i + czynnik < len(T):
            if czy_da_sie(T, S, i + czynnik):
                return True
    return False


N = int(input("N: "))
T = [randint(1, 1000) for _ in range(N)]
S = [0] * N
print(czy_da_sie(T, S, 0))
