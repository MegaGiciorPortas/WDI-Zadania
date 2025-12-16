def zamiana_na_piatkowy(n):
    napis = ""
    while n > 0:
        napis = str(n % 5) + napis
        n //= 5
    if napis == "":
        napis = "0"
    return napis


def czy_ma_17_pokrewnych(T, w, k):
    N = len(T)
    counter = 0

    for i in range(w - 2, w + 3):
        for j in range(k - 2, k + 3):
            if 0 <= i < N and 0 <= j < N:
                if T[w][k] == T[i][j]:
                    counter += 1
    return counter - 1 == 17


# jezeli jest wiecej niz jedno szczesliwe pole w wierszu lub kolumnie
def luck17(T):
    N = len(T)
    wyniki = [[0 for i in range(N)] for _ in range(N)]
    zbiory = []
    for i in range(N):
        tablica = []
        for j in range(N):
            tablica.append(set(zamiana_na_piatkowy(T[i][j])))
        zbiory.append(tablica)

    for i in range(N):
        for j in range(N):
            if czy_ma_17_pokrewnych(zbiory, i, j):
                wyniki[i][j] = 1

    for wiersze in wyniki:
        if sum(wiersze) > 1:
            return True

    for i in range(N):
        suma = 0
        for j in range(N):
            suma += wyniki[j][i]
            if suma > 1:
                return True
    return False
