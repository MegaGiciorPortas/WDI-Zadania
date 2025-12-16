"""
Dane są ciągi: An+1 = sqrt(An*Bn) oraz Bn+1 = (An + Bn)/2.0. Ciągi te są zbieżne do wspól-
nej granicy nazywanej średnią arytmetyczno-geometryczną. Proszę napisać program wyznaczający średnią
arytmetyczno-geometryczną dwóch liczb naturalnych
"""

import math

a = int(input("a: "))
b = int(input("b: "))
eps = 1e-10

while abs(a-b) > eps:
    a, b = math.sqrt(a * b), (a + b) / 2.0

print(round(a, 5))
print(round(b, 5))
