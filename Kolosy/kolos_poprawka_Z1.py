from collections import defaultdict


def possible_moves(N, wspolrzedne):
    slownik = defaultdict(set)
    checker = set(wspolrzedne)
    T = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
    for indeks, krotka in enumerate(wspolrzedne):
        x = krotka[0]
        y = krotka[1]

        for ruch in T:
            new_x = x + ruch[0]
            new_y = y + ruch[1]
            if 0 <= new_x < N and 0 <= new_y < N and (new_x, new_y) not in checker:
                slownik[(x + ruch[0], y + ruch[1])].add(indeks)

    return slownik


def main_function(N, wspolrzedne):
    slownik = possible_moves(N, wspolrzedne)
    ataki = list(slownik.values())

    for i in range(len(ataki)):
        for j in range(i, len(ataki)):
            if len(ataki[i] | ataki[j]) == 7:
                return True
    return False
