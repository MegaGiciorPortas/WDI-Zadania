"""
Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. Ile
różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie. Np.
dla 2315 będą to 21,35,231,315.
"""
from math import log10


def dlugosc_liczby(n):
    wynik = 0
    while n > 0:
        wynik += 1
        n //= 10
    return wynik


def generate_bit_maks(number, dlugosc):
    tablica = [0 for _ in range(dlugosc)]
    indeks = dlugosc - 1

    while number > 0:
        tablica[indeks] = number % 2
        number //= 2
        indeks -= 1

    return tablica


def main_funciton(liczba):
    dlugosc = dlugosc_liczby(liczba)
    cyfry_liczby = [0 for _ in range(dlugosc)]
    indeks = dlugosc - 1
    ilosc_liczb = 0

    while liczba > 0:
        cyfry_liczby[indeks] = liczba % 10
        liczba //= 10
        indeks -= 1

    for number in range(1, 2 ** dlugosc):
        bit_mask = generate_bit_maks(number, dlugosc)

        wynik = 0
        for i in range(len(cyfry_liczby)):
            if bit_mask[i] == 1:
                wynik *= 10
                wynik += cyfry_liczby[i]

        if wynik % 7 == 0:
            ilosc_liczb += 1

    return ilosc_liczb


def rewers_liczby(n):
    dlugosc = int(log10(n)) + 1
    # 51 --> 15
    nowa_liczba = 0
    while n > 0:
        nowa_liczba = nowa_liczba * 10 + n % 10
        n //= 10

    return nowa_liczba


def main_function_v2(n):
    wynik = 0
    dlugosc = int(log10(n)) + 1

    for i in range(1, 2 ** dlugosc):
        kopia = i
        a = n
        x = 0
        for _ in range(dlugosc):
            if i % 2 == 1:
                x = x * 10 + a % 10
            a //= 10
            i //= 2
        x = rewers_liczby(x)
        if x % 7 == 0:
            wynik += 1

    return wynik


n = int(input("n: "))
print(main_funciton(n))
print(main_function_v2(n))
