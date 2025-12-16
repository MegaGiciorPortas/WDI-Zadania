"""
Dla pewnej N-cyfrowej liczby naturalnej obliczono sumę N-tych potęg cyfr tej liczby otrzymu-
jąc kolejną liczbę N-cyfrową. Na przykład dla liczb: 354, 543, 600, ... suma ta wynosi 216. Niestety pierwotna
liczba zaginęła ale wiadomo, że była to największa z możliwych takich liczb. Proszę napisać program, który
na podstawie zachowanej sumy wyznaczy pierwotną liczbę
"""


def suma_cyfr_N_poteg(n, potega):
    suma = 0
    while n > 0:
        suma += (n % 10) ** potega
        n //= 10
    return suma


S = int(input("S: "))
dlugosc = len(str(S))
start = 10 ** dlugosc - 1
meta = 10 ** (dlugosc - 1)
for i in range(start, meta - 1, -1):
    if suma_cyfr_N_poteg(i, dlugosc) == S:
        print(i)
        break
