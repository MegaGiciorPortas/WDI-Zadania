"""
Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.
"""
import math


def fibonacci(n):
    if n <= 0:
        return False
    a = 1
    b = 1

    while b < n:
        a, b = b, a + b

    if b == n:
        return True
    return False


n = int(input("n: "))

a1 = 1
a2 = 1
tablica = []

while a1 <= n:
    tablica.append(a1)
    a1, a2 = a2, a1 + a2

flaga = False

for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        if fibonacci(i) and fibonacci(n // i):
            flaga = True
            break

if flaga:
    print("TAK")
else:
    print("NIE")
