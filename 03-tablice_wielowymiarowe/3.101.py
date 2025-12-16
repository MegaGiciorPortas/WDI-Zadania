"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
element do sumy elementów wiersza w którym leży element jest największa.
"""


def main_function(T):
    N = len(T)
    max_iloraz = 0
    max_wiersz = 0
    max_kolumna = 0

    for i in range(N):
        for j in range(N):
            suma_kolumny = 0
            for k in range(N):
                suma_kolumny += T[k][j]

            suma_wiersza = 0
            for k in range(N):
                suma_wiersza += T[i][k]

            iloraz = suma_kolumny / suma_wiersza
            if iloraz > max_iloraz:
                max_wiersz = i
                max_kolumna = j
                max_iloraz = iloraz

    return max_wiersz, max_kolumna


def main_function_v2(T):
    N = len(T)
    suma_wierszy = [0 for _ in range(N)]
    suma_kolumn = [0 for _ in range(N)]

    for i in range(N):
        for j in range(N):
            suma_wierszy[i] += T[i][j]
            suma_kolumn[j] += T[i][j]

    max_iloraz = -1
    max_wiersz = 0
    max_kolumna = 0

    for i in range(N):
        for j in range(N):
            if suma_kolumn[j] == 0: continue

            if suma_kolumn[j] / suma_wierszy[i] > max_iloraz:
                max_iloraz = suma_kolumn[j] / suma_wierszy[i]
                max_kolumna = j
                max_wiersz = i

    return max_wiersz, max_kolumna


T = [
    [1, 10, 1],
    [1, 10, 1],
    [1, 1, 1]
]

print(main_function(T))
print(main_function_v2(T))
