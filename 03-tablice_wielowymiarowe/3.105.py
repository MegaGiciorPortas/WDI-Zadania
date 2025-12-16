"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
w poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje czy udało
się znaleźć taki ciąg oraz długość tego ciągu.
"""


def main_function(T):
    N = len(T)
    dlugosc_najdluzszego_ciagu = 0

    # najpierw sprawdzenie dla glownej przekatnej i wszystich w dol
    for start in range(N - 2):
        dlugosc = 2
        indeks = 0
        while start + indeks + 2 < N:
            a = T[start + indeks][indeks]
            b = T[start + indeks + 1][indeks + 1]
            c = T[start + indeks + 2][indeks + 2]

            # sprawdzene czy wyrazy to ciag geomatryczny
            if b * b == a * c:
                dlugosc += 1
            else:
                if dlugosc > dlugosc_najdluzszego_ciagu and dlugosc > 2:
                    dlugosc_najdluzszego_ciagu = dlugosc
                dlugosc = 2
            indeks += 1
        if dlugosc > dlugosc_najdluzszego_ciagu and dlugosc > 2:
            dlugosc_najdluzszego_ciagu = dlugosc

    # sprawdzenie dla wszystkich idacych powyzej glownej przekatnej
    for start in range(1, N - 2):
        dlugosc = 2
        indeks = 0
        while start + indeks + 2 < N:
            a = T[indeks][start + indeks]
            b = T[indeks + 1][start + indeks + 1]
            c = T[indeks + 2][start + indeks + 2]

            if b * b == a * c:
                dlugosc += 1
            else:
                if dlugosc > dlugosc_najdluzszego_ciagu and dlugosc > 2:
                    dlugosc_najdluzszego_ciagu = dlugosc
                dlugosc = 2
            indeks += 1
        if dlugosc > dlugosc_najdluzszego_ciagu and dlugosc > 2:
            dlugosc_najdluzszego_ciagu = dlugosc

    if dlugosc_najdluzszego_ciagu > 0:
        return dlugosc_najdluzszego_ciagu
    return None


T1 = [
    [2, 99, 99, 99],
    [99, 4, 99, 99],
    [99, 99, 8, 99],
    [99, 99, 99, 16]
]
T2 = [
    [1, 2, 99],
    [99, 10, 20],  # Ciąg [10, 20] ma dł. 2 (ignorujemy)
    [99, 99, 1]
]
T3 = [
    [1, 2, 4, 8, 99],  # Przekątna [1, 2, 4, 8] -> dł. 4
    [99, 1, 2, 4, 8],  # Przekątna [1, 2, 4, 8] -> dł. 4
    [99, 99, 1, 2, 4],  # Przekątna [1, 2, 4] -> dł. 3
    [99, 5, 0, 0, 0],  # Przekątna [5, 0, 0, 0] -> dł. 4
    [99, 99, 99, 99, 99]
]

print(main_function(T1))
print(main_function(T2))
print(main_function(T3))
