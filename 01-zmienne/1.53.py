"""
Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr wszystkich liczb występujących
w jej rozkładzie na czynniki pierwsze. Na przykład: 85 = 5 ∗17, 8 + 5 = 5 + 1 + 7. Proszę napisać program
wypisujący liczby Smitha mniejsze od 10^6
"""


def sumowanie(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n = n // 10
    return suma


def rozklad(n):
    czynnik = 2
    czynniki = []
    while czynnik * czynnik <= n:
        if n % czynnik == 0:
            czynniki.append(czynnik)
            n = n // czynnik
        else:
            czynnik += 1
    if n > 1:
        czynniki.append(n)

    suma = 0
    for x in czynniki:
        suma += sumowanie(x)
    return suma


def czy_pierwsza(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    return True


licznik = 0
for x in range(2, int(1e6)):
    if not czy_pierwsza(x):
        if sumowanie(x) == rozklad(x):
            print(x)
            licznik += 1
print(licznik)
