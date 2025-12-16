"""
Zadanie 52. Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej licz-
bie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każ-
dej z liczb wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby
12375,17523,75123,17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować
z dwóch zadanych liczb.
"""
from math import log10, floor


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


#
# def funkcja(a, b):
#     napis_a = str(a)
#     napis_b = str(b)
#
#     znalezione_liczby = set()
#
#     def generuj_liczby(reszta_a, reszta_b, stworzona):
#         if not reszta_a and not reszta_b:
#             if stworzona:
#                 znalezione_liczby.add(int(stworzona))
#                 return
#
#         if reszta_a:
#             generuj_liczby(reszta_a[1:], reszta_b, stworzona + reszta_a[0])
#
#         if reszta_b:
#             generuj_liczby(reszta_a, reszta_b[1:], stworzona + reszta_b[0])
#
#     generuj_liczby(napis_a, napis_b, "")
#
#     return znalezione_liczby


def bit_mask(number, l) -> list[int]:
    binary_digits = [0] * l

    indeks = l - 1
    while number > 0:
        binary_digits[indeks] = number % 2
        number //= 2
        indeks -= 1

    return binary_digits


def validate_mask(mask, l1, l2):
    for element in mask:
        if element == 1:
            l1 -= 1
        else:
            l2 -= 1

    return l1 == 0 == l2


def generator_number_from_mask(mask, number1, number2):
    numer = 0
    for element in mask:
        numer *= 10
        if element == 1:
            scalar = 10 ** (length(number1) - 1)
            numer += number1 // scalar
            number1 = number1 % scalar
        else:
            scalar = 10 ** (length(number2) - 1)
            numer += number2 // scalar
            number2 = number2 % scalar

    return numer


def length(number):
    result = 0
    while number > 0:
        result += 1
        number //= 10
    return result


def test52(number1, number2) -> int:
    l1 = floor(log10(number1)) + 1
    l2 = floor(log10(number2)) + 1

    l = l1 + l2

    result = 0
    for i in range(1, 2 ** l):
        mask = bit_mask(i, l)

        if validate_mask(mask, l1, l2):
            number = generator_number_from_mask(mask, number1, number2)
            if czy_pierwsza(number):
                result += 1

    return result

# a = int(input("a: "))
# b = int(input("b: "))
#
# licznik = 0
# stworzone_liczby = funkcja(a, b)
# for liczba in stworzone_liczby:
#     if czy_pierwsza(liczba):
#         licznik += 1
#
# print(licznik)
