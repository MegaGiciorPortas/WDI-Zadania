"""
Proszę napisać program wypisujący podzielniki liczby.

"""
import math

n = int(input("n: "))
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        print(i, int(n / i), end = " ")
