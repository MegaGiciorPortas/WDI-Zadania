"""
Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
wymiarach NxN ruchem skoczka szachowego.
"""
import sys


def drawT(T):
    for line in T:
        for a in line:
            print(a, end = " ")
        print()


def isPossible(T, w, k, i):
    moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    rotation = moves[i]
    nw, nk = w + rotation[0], k + rotation[1]
    if 0 <= nw < len(T) and 0 <= nk < len(T):
        if T[nw][nk] == 0:
            return nw, nk
    return -1, -1


def main_function(T, w = 0, k = 0, counter = 1):
    T[w][k] = counter
    if counter == len(T) ** 2:
        drawT(T)
        exit()
    else:
        for i in range(8):
            newCordinates = isPossible(T, w, k, i)
            if newCordinates != (-1, -1):
                main_function(T, newCordinates[0], newCordinates[1], counter + 1)
    T[w][k] = 0


n = int(input("n: "))
T = [[0 for _ in range(n)] for _ in range(n)]
main_function(T)
