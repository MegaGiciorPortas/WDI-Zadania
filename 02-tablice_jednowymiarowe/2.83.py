"""
Dana jest N-elementowa tablica t zawierająca liczby naturalne mniejsze od 1000. Proszę na-
pisać funkcję, która zwraca długość najdłuższego, spójnego fragmentu tablicy, dla którego w iloczynie jego ele-
mentów każdy czynniki pierwszy występuje co najwyżej raz. Na przykład dla tablicy t=[2,23,33,35,7,4,6,7,5,11,13,22]
wynikiem jest wartość 5
"""
from random import randint

def rozklad_na_czynniki(n):
    """
    Twoja funkcja - poprawnie zwraca listę UNIKALNYCH
    czynników pierwszych. Jest idealna.
    """
    czynniki = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            czynniki.append(i)
            while n % i == 0:
                n //= i
        i += 1

    if n > 1:
        czynniki.append(n)
    return czynniki


def najdluzszy_fragment(T):
    N = len(T)
    if N == 0:
        return 0

    # === Krok 1: Wstępne przetwarzanie (Pre-processing) ===
    # Aby uniknąć obliczania rozkładu w pętli (co jest wolne),
    # obliczamy czynniki dla każdej liczby w T *tylko raz* na początku.
    all_factors = [rozklad_na_czynniki(T[i]) for i in range(N)]

    # === Krok 2: Ustawienie algorytmu "Gąsienicy" ===

    # Ponieważ liczby są < 1000, największy czynnik pierwszy to 997.
    czynniki_count = [0] * 1000

    lewy = 0
    max_dlugosc = 0

    for prawy in range(N):

        # === Krok 3: Rozszerzanie okna (Ruch 'prawy') ===
        nowe_czynniki = all_factors[prawy]

        # === Krok 4: Sprawdź kolizję i kurcz okno (Ruch 'lewy') ===

        # Sprawdzamy, czy którykolwiek z 'nowych' czynników
        # jest już obecny w naszym oknie (licznik > 0).
        jest_kolizja = False
        for c in nowe_czynniki:
            if czynniki_count[c] > 0:
                jest_kolizja = True
                break

        # Dopóki 'nowe_czynniki' kolidują z tym, co już jest w oknie,
        # musimy kurczyć okno od lewej strony.
        while jest_kolizja:
            # Usuń czynniki liczby z LEWEJ strony okna (T[lewy])
            stare_czynniki = all_factors[lewy]
            for c in stare_czynniki:
                czynniki_count[c] -= 1 # Zmniejsz licznik

            lewy += 1 # Przesuń lewy wskaźnik

            # Sprawdź ponownie, czy 'nowe_czynniki' nadal kolidują
            jest_kolizja = False
            for c in nowe_czynniki:
                if czynniki_count[c] > 0:
                    jest_kolizja = True
                    break

        # === Krok 5: Dodaj nowe czynniki do okna ===
        # (Jesteśmy pewni, że nie ma już kolizji)
        for c in nowe_czynniki:
            czynniki_count[c] += 1

        # === Krok 6: Zaktualizuj wynik ===
        aktualna_dlugosc = prawy - lewy + 1
        if aktualna_dlugosc > max_dlugosc:
            max_dlugosc = aktualna_dlugosc

    return max_dlugosc

# --- Uruchomienie ---
N = int(input("N: "))
T = [randint(1, 999) for _ in range(N)]
print(T)

# Przykład z zadania:
# T = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]
# Oczekiwany wynik: 5 (dla [7, 5, 11, 13, 22])

print(najdluzszy_fragment(T))