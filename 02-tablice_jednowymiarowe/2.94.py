"""
Proszę napisać program, który wyznacza wartość pierwiastka kwadratowego z liczby natu-
ralnej x z dokładnością do N miejsc dziesiętnych po przecinku. Program powinien działać poprawnie dla
x<10^8 i N <100
"""
from math import isqrt


def liczenie_pierwiastka_kwadratowego(x, N):
    wynik = ""
    czesc_calkowita = isqrt(x)
    wynik += str(czesc_calkowita) + "."
    reszta = x - czesc_calkowita * czesc_calkowita
    for _ in range(N):
        reszta = reszta * 100
        for d in range(9, -1, -1):
            test_wartosc = d * (20 * czesc_calkowita + d)

            if test_wartosc <= reszta:
                break
        reszta -= test_wartosc
        czesc_calkowita = czesc_calkowita * 10 + d

        wynik += str(d)

    return wynik


x = int(input("x: "))
N = int(input("N: "))
print(liczenie_pierwiastka_kwadratowego(x, N))
