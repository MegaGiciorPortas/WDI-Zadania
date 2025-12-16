"""
Zadanie 37. Proszę napisać program wyliczający pierwiastek równania x^x = 2020 metodą stycznych.
"""
from math import log


def x__x(x):
    return x ** x


def pochodna(x):
    return (log(x) + 1) * x__x(x)


def funkcja(x):
    return x__x(x) - 2020


eps = 1e-12
x = 4.5
diff = -x
while abs(diff) > eps:
    diff = -x
    x = x - funkcja(x) / pochodna(x)
    diff += x

print(x)
