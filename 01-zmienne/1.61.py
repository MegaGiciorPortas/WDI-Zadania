"""
Dana jest liczba naturalna N, którą zapisujemy w systemie o podstawie od 2 do 16. Tak
zapisaną liczbę ”rozcinamy” w dowolnym miejscu na dwa kawałki, a powstałe w ten sposób liczby mnożymy.
Proszę napisać funkcję, która dla liczby N zwróci najmniejszą podstawę systemu, w którym można uzyskać
największy iloczyn, a dodatkowo obie liczby powstałe z podziału są względnie pierwsze. Na przykład: liczba
N = 202 w systemie o podstawie 6 ma postać 534(6). Możliwe podziały w tym systemie o względnie pierw-
szych czynnikach to: 5(6) ∗34(6) i 53(6) ∗4(6) co w systemie o podstawie 10 odpowiada iloczynom: 5∗22 = 110 i
33∗4 = 132. Ten drugi jest największym możliwym do osiągnięcia, a zatem funkcja powinna zwrócić wartość
podstawy równą 6.
"""
from math import log2, floor


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def zamiana_na_system(n, podstawa):
    if n == 0:
        return "0"

    tablica = [0 for _ in range(floor(log2(n)) + 1)]

    indeks = 0
    while n > 0:
        tablica[indeks] = n % podstawa
        n //= podstawa
        indeks += 1

    wynik = ""
    for i in range(indeks - 1, -1, -1):
        if tablica[i] <= 9:
            wynik += str(tablica[i])
        else:
            wynik += chr(tablica[i] + 55)
    return wynik


def powrot_do_dziesietnego(n, podstawa):
    suma = 0
    mnoznik = 0
    for i in range(len(n) - 1, -1, -1):
        if 65 <= ord(n[i]) <= 70:
            suma += (ord(n[i]) - 55) * (podstawa ** mnoznik)
        else:
            suma += int(n[i]) * (podstawa ** mnoznik)
        mnoznik += 1
    return suma


N = int(input("N: "))
najwekszy_iloczyn = 0
najmniejsza_podstawa = 17

for i in range(2, 17):
    nowa_liczba = zamiana_na_system(N, i)

    for j in range(1, len(nowa_liczba)):
        liczba_a_podstawa = nowa_liczba[:j]
        liczba_b_podsstawa = nowa_liczba[j:]
        liczba_a = powrot_do_dziesietnego(liczba_a_podstawa, i)
        liczba_b = powrot_do_dziesietnego(liczba_b_podsstawa, i)

        if nwd(liczba_a, liczba_b) == 1:
            iloczyn = liczba_a * liczba_b

            if iloczyn > najwekszy_iloczyn:
                najwekszy_iloczyn = iloczyn
                najmniejsza_podstawa = i

print(najmniejsza_podstawa)
