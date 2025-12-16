"""
Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby
są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje wyłącznie z
przyjaciółkami
"""


def czy_spelnia_warunki_zadania(T, wiersz, kolumna):
    N = len(T)

    if wiersz - 1 > 0:
        gora_poprawny_wiersz = True
    else:
        gora_poprawny_wiersz = False
    if wiersz + 1 < N:
        dol_poprawny_wiersz = True
    else:
        dol_poprawny_wiersz = False
    if kolumna - 1 > 0:
        lewo_poprawna_kolumna = True
    else:
        lewo_poprawna_kolumna = False
    if kolumna + 1 < N:
        prawo_poprawna_kolumna = True
    else:
        prawo_poprawna_kolumna = False

    # [] [] []
    # [] [srodek] []
    # [] [] []

    srodek = T[wiersz][kolumna]
    czy_sasiedzi_przyajciele = True
    if gora_poprawny_wiersz and lewo_poprawna_kolumna:
        if

def main_function(T):
    N = len(T)

    zbiory_liczb = [[set() for _ in range(N)] for _ in range(N)]
    for wiersz in range(N):
        for kolumna in range(N):
            zbiory_liczb[wiersz][kolumna] = set(T[wiersz][kolumna])

    liczba_elementow = 0
    for wiersz in range(N):
        for kolumna in range(N):
            if czy_spelnia_warunki_zadania(zbiory_liczb, wiersz, kolumna):
                liczba_elementow += 1
