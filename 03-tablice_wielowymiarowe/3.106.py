"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
w poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.
"""


def main_function(T, k):
    N = len(T)

    for size in range(3, N, 2):
        for wiersz in range(N - size + 1):
            for kolumna in range(N - size + 1):
                iloczyn = 1
                iloczyn *= T[wiersz][kolumna]
                iloczyn *= T[wiersz][kolumna + size - 1]
                iloczyn *= T[wiersz + size - 1][kolumna]
                iloczyn *= T[wiersz + size - 1][kolumna + size - 1]

                if iloczyn == k:
                    return wiersz + (size // 2), kolumna + (size // 2)

    return -1. - 1


T = []
k = 0

wiersz, kolumna = main_function(T,k)
if wiersz == -1 and kolumna == -1:
    print("Nie znaleziono punktu!")
else:
    print("Znaleziono punkt")
    print(f"Wsplrzedne: ({wiersz},{kolumna})")

