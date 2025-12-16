"""
Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne. Z wartości w
obu tablicach możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element
(z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8. Proszę napisać funkcje generującą
i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi. Do funkcji należy przekazać dwie
tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum
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


def func(T1, T2):
    aktualne_sumy = {T1[0], T2[0], T1[0] + T2[0]}

    for i in range(1, len(T1)):
        possible_sums = [T1[i], T2[i], T1[i] + T2[i]]
        new_sums = set()

        for s in possible_sums:
            for v in aktualne_sumy:
                new_sums.add(s + v)
        aktualne_sumy = new_sums

    licznik = 0
    for x in aktualne_sumy:
        if czy_pierwsza(x):
            licznik += 1

    return licznik


N = int(input("N: "))
T1 = [randint(1, 10) for _ in range(N)]
T2 = [randint(1, 10) for _ in range(N)]

print(func(T1, T2))
