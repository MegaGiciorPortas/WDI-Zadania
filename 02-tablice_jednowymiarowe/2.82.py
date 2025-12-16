"""
Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
"""

from random import randint


def funkcja(T):
    N = len(T)
    najdluzsza_dlugosc = 0

    # Pętla zewnętrzna (i = indeks startowy)
    for i in range(N):

        # Resetujemy sumy dla każdego nowego podciągu
        suma_wartosci = 0
        suma_indeksow = 0

        # Pętla wewnętrzna (j = indeks końcowy)
        for j in range(i, N):

            # --- Warunek 1: Czy ciąg jest nadal rosnący? ---
            if j > i and T[j] <= T[j - 1]:
                # j > i (pilnuje, by nie sprawdzać T[i] z T[i-1])
                # T[j] <= T[j-1] (warunek rosnący złamany)
                break  # Przerwij pętlę 'j', zacznij od nowego 'i'

            # --- Warunek 2: Dodaj wartości ---
            # Jeśli warunek rosnący jest OK (lub j==i), dodaj
            suma_wartosci += T[j]
            suma_indeksow += j

            # --- Warunek 3: Sprawdź sumy ---
            # Ten 'if' obsługuje zarówno długość 1 (gdy j==i),
            # jak i długości większe.
            if suma_wartosci == suma_indeksow:

                # POPRAWNA KALKULACJA DŁUGOŚCI
                aktualna_dlugosc = j - i + 1

                if aktualna_dlugosc > najdluzsza_dlugosc:
                    najdluzsza_dlugosc = aktualna_dlugosc

    return najdluzsza_dlugosc


# --- Uruchomienie ---
N = int(input("N: "))
T = [randint(1, 100) for _ in range(N)]
print(T)

print(funkcja(T))
