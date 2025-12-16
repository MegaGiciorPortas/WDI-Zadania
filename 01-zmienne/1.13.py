"""
Proszę napisać program wypisujący rozkład liczby na czynniki pierwsze.
"""
from math import sqrt

n = int(input("n: "))

i = 2
while i <= sqrt(n):
    if n % i == 0:
        print(i)
        n = n // i
    else:
        i += 1
if n > 1:
    print(n)
