"""
Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
wartość sumy, funkcja powinna zwrócić wartość typu bool.
"""
from random import randint


def recurension(T, suma, kolumny, current = 0, indeks = 0):
    if indeks == 8:
        return current == suma

    if current > suma:
         return False

    if current == suma and current > 0:
        return True


    for i in range(8):
        if kolumny[i] == 0:
            kolumny[i] = 1
            if recurension(T, suma, kolumny, current + T[indeks][i], indeks + 1):
                return True
            kolumny[i] = 0
    if recurension(T,suma,kolumny,current,indeks+1):
        return True
    return False


def main_funciton(T, suma) -> bool:
    kolumny = [0 for _ in range(8)]
    result = recurension(T, suma, kolumny)
    return result


T = [[randint(0, 9) for _ in range(8)] for _ in range(8)]
suma = randint(0,99)
print(f"{suma} {main_funciton(T,suma)}")
