"""
Mamy dane dwa ciągi A,B o następujących zależnościach:
A: a0 = 0,a1 = 1,an = an−1−bn−1 ∗an−2
B: b0 = 2,bn = bn−1 + 2 ∗an−1
Proszę napisać program, który czyta liczby typu int ze standardowego wejścia i tak długo jak liczby te są
kolejnymi wyrazami ciągu An (tj. a0,a1,a2, ...) wypisuje na standardowe wyjście wyrazy drugiego ciągu Bn
(tj. b0,b1,b2, ...)
"""


def An(an_1, an_2, bn_1):
    return an_1 - bn_1 * an_2


def Bn(bn_1, an_1):
    return bn_1 + 2 * an_1


a_2 = 0
a_1 = 1
b_1 = 2
licznik = 0

wynik = ""
while True:
    try:
        wpisana = int(input("Podaj: "))
    except  ValueError:
        break
    if licznik == 0:
        licznik += 1
        if wpisana != 0:
            break
        wynik += "2 "
    elif licznik == 1:
        licznik += 1
        if wpisana != 1:
            break
        b_1 = Bn(2, 0)
        wynik += f"{str(b_1)} "
    else:
        a_1, a_2 = An(a_1, a_2, b_1), a_1
        if wpisana != a_1:
            break
        b_1 = Bn(b_1, a_2)
        wynik += f"{str(b_1)} "

print(wynik.rstrip())