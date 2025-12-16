"""
Proszę napisać program wczytujący liczbę naturalną i rozkładający ją na iloczyn 2 liczb o
najmniejszej różnicy. Na przykład: 30 = 5 ∗6, 120 = 10 ∗12.
"""
from math import isqrt

n = int(input("n: "))

for i in range(isqrt(n), 0, -1):
    if n % i == 0:
        print(i, n // i)
        break

