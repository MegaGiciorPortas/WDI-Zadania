"""
Zadanie 56. Dwie liczby naturalne są różno-cyfrowe jeżeli nie posiadają żadnej wspólnej cyfry. Proszę na-
pisać program, który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu (w zakresie
2−16) w którym liczby są różno-cyfrowe. Program powinien wypisać znalezioną podstawę, jeżeli podstawa
taka nie istnieje należy wypisać komunikat o jej braku. Na przykład: dla liczb 123 i 522 odpowiedzią jest
podstawa 11 bo 123(10) = 102(11) i 522(10) = 435(11).
"""
from math import log2, ceil


def func(n, s):
    N = ceil(log2(n)) + 1
    t = [0 for _ in range(N)]
    index = 0
    while n > 0:
        t[index] = n % s
        n = n // s
        index += 1

    wynik = ""
    for i in range(index - 1, -1, -1):
        if t[i] >= 10:
            wynik += chr((t[i] % 10) + 65)
        else:
            wynik += str(t[i])

    return set(wynik)


a = int(input("a: "))
b = int(input("b: "))
wynik = 0

for i in range(2, 17):
    new_a = func(a, i)
    new_b = func(b, i)

    if new_a.isdisjoint(new_b):
        wynik = i
        break

if wynik != 0:
    print(wynik)
else:
    print("Nie ma takiego systemu! ")