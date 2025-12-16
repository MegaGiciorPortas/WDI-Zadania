"""
Zadanie 54. Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników
niż 2,3,5. Jedynka też jest taką liczbą. Proszę napisać program, który wylicza ile takich liczb znajduje się w
przedziale od 1 do N włącznie.
"""


def czy_spelnia_kryteria(n):
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //= 5

    return n == 1


n = int(input("n: "))
licznik = 0
for i in range(2, n + 1):
    if czy_spelnia_kryteria(i):
        licznik += 1

print(licznik)
