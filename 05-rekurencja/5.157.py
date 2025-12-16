"""
Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki.
"""


def findENEK(T, X, K, indeks = 0, iloczyn = 1, elementy = 0, interior = ""):
    if iloczyn > X or elementy > K:
        return
    if elementy == K:
        if iloczyn == X:
            print(interior[:-1])
        return
    if indeks == len(T):
        return

    findENEK(T, X, K, indeks + 1, iloczyn * T[indeks], elementy + 1, interior + f"{str(T[indeks])}*")
    findENEK(T, X, K, indeks + 1, iloczyn, elementy, interior)
    return


X = int(input("X: "))
K = int(input("K: "))
T = [1, 2, 3, 4, 6, 7, 8, 11]
findENEK(T, X, K)
