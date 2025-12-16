"""
Dana jest tablica T zawierająca liczby wymierne reprezentowane w postaci ułamków. Ułam-
ki reprezentowane są w postaci krotek składających się z licznika i mianownika. Proszę napisać funkcję
longest(T), zwracającą długość najdłuższego spójnego podciągu, którego elementy stanowią ciąg geome-
tryczny. W przypadku, gdy w tablicy nie ma ciągu dłuższego niż 2 elementy, funkcja powinna zwrócić wartość
0.
Przykłady:
print(longest( [(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)] ) # wypisze 4
print(longest( [(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)] ) # wypisze 3
print(longest( [(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)] ) # wypisze 6
print(longest( [(1,2),(2,3),(3,4),(4,5),(5,6)] ) # wypisze 0
"""


def longest(T):
    najdluzszy_podciag = 0
    dlugosc = 2

    for i in range(2, len(T)):
        a = T[i - 2]
        b = T[i - 1]
        c = T[i]

        # (b[0]/b[1])/(a[0]/a[1]) == (c[0]/c[1])/(b[0]/b[1])
        # (b[0])^2 / (b[1])^2 == (a[0]*c[0]) / (a[1]*c[1])
        # b[1]^2 * a[0]*c[0] == b[0]^2 * a[1]*c[1]
        if b[1] * b[1] * a[0] * c[0] == b[0] * b[0] * a[1] * c[1]:
            dlugosc += 1
        else:
            if dlugosc > najdluzszy_podciag and dlugosc > 2:
                najdluzszy_podciag = dlugosc
            dlugosc = 2
    if dlugosc > 2 and dlugosc > najdluzszy_podciag:
        najdluzszy_podciag = dlugosc

    return najdluzszy_podciag


print(longest([(0, 2), (1, 2), (2, 2), (4, 2), (4, 1), (5, 1)]))  # wypisze 4
print(longest([(1, 2), (-1, 2), (1, 2), (1, 2), (1, 3), (1, 2)]))  # wypisze 3
print(longest([(3, 18), (-1, 6), (7, 42), (-1, 6), (5, 30), (-1, 6)]))  # wypisze 6
print(longest([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]))  # wypisze 0
