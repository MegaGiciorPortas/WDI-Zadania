"""
Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.

"""
from math import log2, floor


def func(n, s):
    if n < 2:
        print(n)
    else:
        N = floor(log2(n)) + 1
        t = [0 for _ in range(N)]
        index = 0
        while n > 0:
            t[index] = n % s
            n = n // s
            index += 1

        for i in range(index - 1, -1, -1):
            if t[i] >= 10:
                print(chr(t[i] - 10 + 65), end = "")
            else:
                print(t[i], end = "")


n = int(input("n: "))
s = int(input("system: "))

func(n, s)
