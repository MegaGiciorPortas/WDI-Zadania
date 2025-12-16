"""
Dana jest tablica T zawierająca liczby wymierne reprezentowane w postaci ułamków. Ułamki
reprezentowane są w postaci krotek składających się z licznika i mianownika. Proszę napisać funkcję zwraca-
jącą długość najdłuższego spójnego podciągu, którego elementy stanowią ciąg geometryczny. W przypadku
gdy w tablicy nie ma takiego podciągu dłuższego niż 2 elementy, funkcja powinna zwrócić wartość 0. Można
założyć, że tablica wejściowa liczy więcej niż 2 elementy
"""


def szukanie_najdluzszego_podciagu(T):
    najdluzszy_podciag = 0
    dlugosc = 2

    for i in range(2, len(T)):
        krotka1 = T[i - 2]
        krotka2 = T[i - 1]
        krotka3 = T[i]

        a, b = krotka1[0], krotka1[1]
        c, d = krotka2[0], krotka2[1]
        e, f = krotka3[0], krotka3[1]

        if c * c * b * f == d * d * e * a:
            dlugosc += 1
        else:
            if dlugosc > najdluzszy_podciag:
                najdluzszy_podciag = dlugosc
            dlugosc = 2

    if dlugosc > najdluzszy_podciag:
        najdluzszy_podciag = dlugosc

    if najdluzszy_podciag <= 2:
        return 0
    return najdluzszy_podciag


T = [
    (1, 1),  # 0: Wartość 1
    (2, 1),  # 1: Wartość 2
    (4, 1),  # 2: Wartość 4
    (8, 1),  # 3: Wartość 8
    (1, 5),  # 4: Wartość 1/5
    (10, 1),  # 5: Wartość 10 (przerywnik)
    (27, 2),  # 6: Wartość 13.5
    (18, 2),  # 7: Wartość 9
    (12, 2)  # 8: Wartość 6
]

T1 = [
    (1, 2),  # 0: Wartość 0.5
    (1, 4),  # 1: Wartość 0.25
    (9, 1),  # 2: Wartość 9 (przerywnik)
    (5, 1),  # 3: Wartość 5
    (5, 2),  # 4: Wartość 2.5
    (1, 10),  # 5: Wartość 0.1
    (1, 100)  # 6: Wartość 0.01
]

T2 = [
    (2, 1),  # 0: Wartość 2
    (-4, 1),  # 1: Wartość -4
    (8, 1),  # 2: Wartość 8
    (-16, 1),  # 3: Wartość -16
    (99, 1),  # 4: Wartość 99 (przerywnik)
    (7, 1),  # 5: Wartość 7
    (7, 1),  # 6: Wartość 7
    (7, 1),  # 7: Wartość 7
    (5, 1),  # 8: Wartość 5
    (0, 1),  # 9: Wartość 0
    (0, 1),  # 10: Wartość 0
    (9, 1)  # 11: Wartość 9
]
print(szukanie_najdluzszego_podciagu(T))
print(szukanie_najdluzszego_podciagu(T1))
print(szukanie_najdluzszego_podciagu(T2))
