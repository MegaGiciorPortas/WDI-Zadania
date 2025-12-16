"""
Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe.
"""
from random import randint


def rozklad_na_czynniki(n) -> list:
    kopia = n
    tablica = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            tablica.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1 and n != kopia:
        tablica.append(n)
    return tablica

minimalna_liczba_ruchow = float('inf')

def rekurencja(T, N, indeks = 0, moves = 0) -> int:
    global minimalna_liczba_ruchow

    if indeks == N-1:
        if moves < minimalna_liczba_ruchow:
            minimalna_liczba_ruchow = moves
        return

    if moves >= minimalna_liczba_ruchow:
        return

    czynniki = rozklad_na_czynniki(T[indeks])

    for number in czynniki:
        if indeks + number < N:
            rekurencja(T,N,indeks+number, moves + 1)


def main_function(T):
    global minimalna_liczba_ruchow
    N = len(T)
    rekurencja(T,N)
    if minimalna_liczba_ruchow == float('inf'):
        return -1
    return minimalna_liczba_ruchow


def rekurencja_czysta(T, N, indeks):
    # 1. BASE CASE: Jesteśmy na mecie
    if indeks == N - 1:
        return 0  # Jesteśmy na miejscu, więc koszt to 0 dodatkowych kroków

    czynniki = rozklad_na_czynniki(T[indeks])

    # Jeśli ślepa uliczka (brak czynników), zwracamy nieskończoność
    if not czynniki:
        return float('inf')

    # Szukamy najkrótszej drogi spośród wszystkich możliwych skoków
    najlepsza_sciezka_stad = float('inf')

    for skok in czynniki:
        if indeks + skok < N:
            # Pytamy rekurencję: ile kroków z TAMTEGO miejsca do końca?
            wynik_dziecka = rekurencja_czysta(T, N, indeks + skok)

            # Jeśli dziecko znalazło drogę (wynik != inf), to porównujemy
            if wynik_dziecka != float('inf'):
                najlepsza_sciezka_stad = min(najlepsza_sciezka_stad, wynik_dziecka)

    # 2. ZWRACANIE WYNIKU (Kluczowy moment)
    # Jeśli nic nie znaleźliśmy, zwracamy inf.
    if najlepsza_sciezka_stad == float('inf'):
        return float('inf')

    # W przeciwnym razie: 1 (mój skok) + to co znalazło najlepsze dziecko
    return 1 + najlepsza_sciezka_stad


def main_czysta(T):
    wynik = rekurencja_czysta(T, len(T), 0)

    if wynik == float('inf'):
        return -1
    return wynik


N = randint(2, 100)
T = [randint(1, 100) for _ in range(N)]
print(main_function(T))