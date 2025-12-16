"""
Dana jest duża tablica T. Proszę napisać funkcję, która zwraca informację czy w tablicy
zachodzi następujący warunek: „wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są
liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą
"""
from random import randint


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


def indeksy_fibonacciego(n):
    tablica = [0 for _ in range(n + 1)]
    tablica[0] = 1
    a1 = 1
    a2 = 1

    while a2 <= n:
        a1, a2 = a2, a1 + a2
        tablica[a1] = 1
    return tablica


def sprawdzanie_obu_warunkow(T, F):
    warunek_pierwszy = True
    warunek_drugi = False

    for i in range(len(T)):
        if F[i] == 1:
            if czy_pierwsza(T[i]):
                return False
        else:
            if czy_pierwsza(T[i]):
                warunek_drugi = True

    return warunek_pierwszy and warunek_drugi


N = int(input("N: "))
T = [randint(1, 1000) for _ in range(N)]
Fibonacci = indeksy_fibonacciego(N)

print(sprawdzanie_obu_warunkow(T, Fibonacci))
