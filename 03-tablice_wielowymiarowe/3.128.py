"""
Tablica T[N][N] zawiera liczby naturalne. Proszę napisać funkcję select(T), która wybiera
z tablicy dowolne N parami różnych elementów tak aby:
• żadne dwa wybrane elementy nie leżały w tej samej kolumnie ani wierszu,
• suma wybranych elementów powinna mieścić się w przedziale [2000,2025].
Funkcja powinna zwrócić wartość sumy wybranych elementów albo wartość None, jeżeli taki wybór nie jest
możliwy
"""
def rekurencja(T,usedKolumns,result = 0,indeks = 0):
    N = len(T)

    if indeks == N:
        if 2000 <= result <= 2025:
            return result
        return None

    if result > 2025:
        return None

    for i in range(N):
        if usedKolumns[i] != 1:
            usedKolumns[i] = 1
            wynik = rekurencja(T,usedKolumns,result + T[indeks][i],indeks + 1)
            if wynik is not None:
                return wynik
            usedKolumns[i] = 0
    return None


def main_function(T):
    N = len(T)
    usedKolumns = [0 for _ in range(N)]
    wynik = rekurencja(T,usedKolumns)
    return wynik



def testuj(nazwa, T, oczekiwany_wynik):
    print(f"--- TEST: {nazwa} ---")
    try:
        wynik = main_function(T)

        # Jeśli oczekujemy konkretnej liczby (sukces)
        if isinstance(oczekiwany_wynik, int):
            if wynik == oczekiwany_wynik:
                print(f"✅ SUKCES! Wynik: {wynik}")
            elif wynik is not None and 2000 <= wynik <= 2025:
                # Czasami jest wiele poprawnych kombinacji,
                # więc jeśli wynik mieści się w przedziale, to też jest OK.
                print(f"✅ SUKCES! Wynik: {wynik} (mieści się w przedziale, choć test celował w {oczekiwany_wynik})")
            else:
                print(f"❌ BŁĄD. Otrzymano: {wynik}, Oczekiwano: {oczekiwany_wynik} (lub liczby z [2000, 2025])")

        # Jeśli oczekujemy None (porażka)
        else:
            if wynik is None:
                print(f"✅ SUKCES! Wynik: None")
            else:
                print(f"❌ BŁĄD. Otrzymano: {wynik}, Oczekiwano: None")

    except Exception as e:
        print(f"❌ WYJĄTEK (Błąd w kodzie): {e}")
    print("-" * 30)


# ==========================================
# SCENARIUSZE TESTOWE
# ==========================================

T1 = [
    [2000, 100, 100],
    [100, 10, 100],
    [100, 100, 5]
]
testuj("Prosta przekątna", T1, 2015)

T2 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
testuj("Za mała suma", T2, None)

T3 = [
    [3000, 3000, 3000],
    [3000, 3000, 3000],
    [3000, 3000, 3000]
]
testuj("Za duża suma", T3, None)

T4 = [
    [2000, 1000, 1000],
    [10, 1000, 1000],
    [5, 1000, 1000]
]
testuj("Kolizja w kolumnie (wszystkie dobre w jednej linii)", T4, 2010)

T5 = [
    [9000, 1000, 9000],
    [1000, 9000, 9000],
    [9000, 9000, 15]
]
testuj("Wymuszony zygzak", T5, 2015)

T6 = [
    [1998, 9999],
    [9999, 2]
]
# Wybór: (0,0) i (1,1) -> 1998 + 2 = 2000
testuj("Dolna granica (2000)", T6, 2000)