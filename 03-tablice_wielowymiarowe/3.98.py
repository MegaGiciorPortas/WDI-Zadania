'''
Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami naturalnymi po spirali.

[1][2][3][4]
[12][13][14][5]
[11][16][15][6]
[10][9][8][7]
'''


def spirala(T):
    N = len(T)
    k = 1
    a, b = 0, N - 1
    while a <= b:
        if a == b:
            T[a][b] = k
            break
        for i in range(a, b):
            T[a][i] = k
            k += 1
        for i in range(a, b):
            T[i][b] = k
            k += 1
        for i in range(b, a, -1):
            T[b][i] = k
            k += 1
        for i in range(b, a, -1):
            T[i][a] = k
            k += 1

        a += 1
        b -= 1


N = int(input("N: "))
T = [[0 for i in range(N)] for _ in range(N)]
spirala(T)
for i in range(len(T)):
    print(T[i])
