"""
Liczba doskonała to liczba równa sumie swoich podzielników właściwych (mniejszych od
jej samej), na przykład 6 = 1 + 2 + 3. Proszę napisać program wyszukujący liczby doskonałe mniejsze od
miliona.
"""

import math


def czy_doskonala(n):
    suma = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            suma += i
            if i != n % i:
                suma += n // i

    if suma == n:
        return True
    return False


for i in range(2, int(1e6)):
    if czy_doskonala(i):
        print(i)
