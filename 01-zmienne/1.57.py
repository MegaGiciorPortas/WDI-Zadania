"""
Zadanie 57. „Obcięcie” liczby naturalnej polega na usunięciu z niej M początkowych i N końcowych
cyfr, gdzie M,N >= 0. Proszę napisać funkcję, która dla danej liczby naturalnej K zwraca największą liczbę
pierwszą o różnych cyfrach jaką można uzyskać z obcięcia liczby K albo 0 gdy taka liczba nie istnieje. Na
przykład dla liczby 1202742516 spośród obciętych liczb pierwszych: 2,5,7,251,2027 liczbą spełniającą warunek
jest liczba 251.
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
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    return True


def czy_rozne_liczby(n):
    return len(list(n)) == len(set(n))


def funkcja(napis):
    wynik = 0
    for lewy in range(len(napis)):
        prawy = len(napis)
        while prawy > lewy:
            liczba = int(napis[lewy:prawy])
            if czy_rozne_liczby(str(liczba)) and czy_pierwsza(liczba):
                if liczba > wynik:
                    wynik = liczba
            prawy -= 1
    return wynik


napis = input("napis: ")
print(funkcja(napis))
