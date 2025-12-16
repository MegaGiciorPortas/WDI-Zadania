"""
Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi
zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i
kolumnie k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy
minimalny koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt
przebywania na polu startowym i ostatnim także wliczamy do kosztu przejścia.
"""
from random import randint


def koszt(T, k, r = 0) -> int:
    if k < 0 or k > 7:
        return float('inf')
    if r == 7:
        return T[r][k]
    return T[r][k] + min(koszt(T, k, r + 1), koszt(T, k - 1, r + 1), koszt(T, k + 1, r + 1))


minCost = float('inf')


def zadanie(T, k, r = 0, sum = 0) -> None:
    global minCost
    if r == 8:
        minCost = min(minCost, sum)
        return

    zadanie(T, k, r + 1, sum + T[r][k])
    if k > 0:   zadanie(T, k - 1, r + 1, sum + T[r][k])
    if k < 7:   zadanie(T, k + 1, r + 1, sum + T[r][k])


def rozwiaznaie(T, k) -> int:
    global minCost
    zadanie(T, k)
    return minCost


T = [[randint(1, 1000) for _ in range(8)] for _ in range(8)]
k = randint(0, 7)

print(rozwiaznaie(T, k))
print(koszt(T, k))
