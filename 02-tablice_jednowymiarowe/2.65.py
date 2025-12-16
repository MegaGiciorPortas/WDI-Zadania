"""
Napisać funkcje sprawdzającą czy dwie liczby naturalne są one zbudowane z takich samych
cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.
"""


def cyfra_na_tablice(n):
    if n == 0:
        return [0]

    dl = 0
    temp = n
    while temp > 0:
        temp //= 10
        dl += 1

    tablica = [0 for _ in range(dl)]
    for i in range(dl):
        tablica[i] = n % 10
        n //= 10

    return tablica


def func(n1, n2):
    t1 = cyfra_na_tablice(n1)
    t2 = cyfra_na_tablice(n2)

    if len(t1) != len(t2):
        return False

    t1.sort()
    t2.sort()

    for i in range(len(t1)):
        if t1[i] != t2[i]:
            return False
    return True


n1 = int(input("n1: "))
n2 = int(input("n2: "))

print(func(n1, n2))
