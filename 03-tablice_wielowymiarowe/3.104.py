"""
Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M],
gdzie M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza)
liczby naturalne. Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w
tablicy T2 były uporządkowane niemalejąco.
"""


def main_function(T):
    N = len(T)
    wynik = [0 for _ in range(N * N)]

    aktualny_indeks_kolumny = [0 for _ in range(N)]

    for iterator in range(N * N):
        aktualne_wartosci = [0 for _ in range(N)]

        for i in range(N):
            if aktualny_indeks_kolumny[i] != N:
                aktualne_wartosci[i] = T[i][aktualny_indeks_kolumny[i]]
            else:
                aktualne_wartosci[i] = -1

        indeks = 0
        while True:
            if aktualne_wartosci[indeks] != -1:
                najmniejsza_wartosc = aktualne_wartosci[indeks]
                najmnieszy_indeks = indeks
                break
            indeks += 1

        for i in range(indeks + 1, N):
            if aktualne_wartosci[i] < najmniejsza_wartosc and aktualne_wartosci[i] != -1:
                najmniejsza_wartosc = aktualne_wartosci[i]
                najmnieszy_indeks = i

        wynik[iterator] = najmniejsza_wartosc
        aktualny_indeks_kolumny[najmnieszy_indeks] += 1

    return wynik


T = [
    [1, 2, 8],
    [2, 3, 5],
    [1, 2, 7]
]

print(main_function(T))
