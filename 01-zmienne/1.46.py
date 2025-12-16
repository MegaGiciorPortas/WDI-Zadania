"""
Dane są dwie liczby naturalne, m i n. Proszę napisać program, który wyznacza sumę n
kolejnych cyfr po przecinku rozwinięcia dziesiętnego liczby sqrt(m)
"""

from math import isqrt

n = int(input("n: "))
m = int(input("m: "))

s = str(isqrt(m * 10 ** (2 * n)))
dlugosc_calkowita = len(str(isqrt(m)))
suma = 0
print(s[dlugosc_calkowita:])
for x in s[dlugosc_calkowita:]:
    suma += int(x)
print(suma)
