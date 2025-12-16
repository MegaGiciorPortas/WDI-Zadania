"""
Zadanie 59. Proszę napisać program znajdujący jak najwięcej liczb N-cyfrowych dla których suma N-
tych potęg cyfr liczby jest równa tej liczbie, np. 153 = 1^3 + 5^3 + 3^3
"""


def funkcja(n, tablica):
    temp = n
    suma = 0
    while temp > 0:
        a = temp % 10
        suma += tablica[a]
        temp //= 10
    return suma == n


def tablica_poteg(potega):
    tablica = [0 for _ in range(10)]

    for indeks in range(len(tablica)):
        tablica[indeks] = indeks ** potega

    print(tablica)
    return tablica


N = int(input("N: "))
start = 10 ** (N - 1)
meta = 10 ** N
potegi_cyfr = tablica_poteg(N)

licznik = 0
for i in range(start, meta):
    if funkcja(i, potegi_cyfr):
        licznik += 1

print(licznik)
