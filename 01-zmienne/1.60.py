"""
Tylko 7 liczb pierwszych spełnia warunek z poprzedniego zadania. Proszę napisać program
znajdujacy wszystkie te liczby
"""

# tutaj jest chyba taki problem ze istnieja tylko takie 4 liczby i dalej program nie znajduje
# ale ofc moge sie mylic

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


def czy_suma_sie_zgadza(n, tablica):
    temp = n
    suma = 0

    while temp > 0:
        suma += tablica[temp % 10]
        temp //= 10

    return suma == n


def tworzenie_tablicy(N):
    tablica = [i ** N for i in range(10)]
    return tablica


licznik_znalezionych = 0
for N in range(1, 62):
    tablica_poteg = tworzenie_tablicy(N)

    if N == 1:
        start = 1
        meta = 10
    else:
        start = 10 ** (N - 1)
        meta = 10 ** N

    for liczba in range(start, meta):
        if czy_suma_sie_zgadza(liczba, tablica_poteg):
            if czy_pierwsza(liczba):
                licznik_znalezionych += 1
                print(liczba)

