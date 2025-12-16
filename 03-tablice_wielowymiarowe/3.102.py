"""
Poprzednie zadanie z tablicą wypełnioną liczbami całkowitymi.
"""


def main_function(T):
    N = len(T)
    suma_wierszy = [0 for _ in range(N)]
    suma_kolumn = [0 for _ in range(N)]

    for i in range(N):
        for j in range(N):
            suma_wierszy[i] += T[i][j]
            suma_kolumn[j] += T[i][j]

    max_wiersz = 0
    max_kolumna = 0

    for i in range(N):
        for j in range(N):
            if suma_wierszy[i] == 0: continue

            aktualny_iloraz = suma_kolumn[j] / suma_wierszy[i]

            if suma_kolumn[j] / suma_wierszy[i] > max_iloraz or max_iloraz is None:
                max_iloraz = suma_kolumn[j] / suma_wierszy[i]
                max_kolumna = j
                max_wiersz = i

    if max_iloraz is None:
        return None

    return max_wiersz, max_kolumna


T = []
print(main_function(T))
