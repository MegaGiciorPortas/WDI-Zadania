from copy import deepcopy


def diagonal_sum(T):
    prawa = 0
    lewa = 0
    for i in range(4):
        prawa += T[i][i]
        lewa += T[i][3 - i]
    return lewa == prawa


def possible_moves(wspolrzedne):
    x, y = wspolrzedne[0], wspolrzedne[1]
    tablica = []
    if x - 1 >= 0:
        tablica.append((x - 1, y))
    if x + 1 <= 3:
        tablica.append((x + 1, y))
    if y - 1 >= 0:
        tablica.append((x, y - 1))
    if y + 1 <= 3:
        tablica.append((x, y + 1))

    return tablica


def recurension(T, k, moves = 0, wspolrzedne = (3, 3), poprzedni = (0, 0)):
    if diagonal_sum(T):
        return True

    if moves >= k:
        return False

    possible = possible_moves(wspolrzedne)
    for krotka in possible:
        if krotka != poprzedni:
            kopia = deepcopy(T)
            T[wspolrzedne[0]][wspolrzedne[1]] = T[krotka[0]][krotka[1]]
            T[krotka[0]][krotka[1]] = 0
            if recurension(T, k, moves + 1, krotka, wspolrzedne):
                return True
            T = kopia
    return False


def sol(T, k):
    return recurension(T, k)
