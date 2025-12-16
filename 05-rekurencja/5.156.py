"""
Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie
"""


def findENEK(T, X, K, indeks = 0, iloczyn = 1, elementy = 0):
    if iloczyn > X or elementy > K:
        return 0
    if elementy == K:
        if iloczyn == X:
            return 1
        return 0
    if indeks == len(T):
        return 0


    return findENEK(T, X, K, indeks + 1, iloczyn * T[indeks], elementy + 1) + findENEK(T, X, K, indeks + 1, iloczyn,
                                                                                       elementy)


X = int(input("X: "))
K = int(input("K: "))
T = [1, 2, 3, 4, 5, 7, 8, 11]
print(findENEK(T, X, K))
