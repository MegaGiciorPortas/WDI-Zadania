"""
Dana jest plansza o wymiarach NxN zawierająca wartości 0 i 1. Pola o wartości 1 zawierają
pułapki. Skoczek musi dotrzeć z górnego wiersza planszy do dolnego. Każdy ruch skoczka musi go przybliżać
do dolnego wiersza. Proszę napisać program, który zwraca długość najkrótszej bezpiecznej drogi skoczka z
wiersza górnego do wiersza dolnego
"""
from random import randint


def isPossible(T, w, k, i):
    tablica = [(1, 2), (2, 1), (1, -2), (2, -1)]
    current_move = tablica[i]
    newW = w + current_move[0]
    newK = k + current_move[1]
    if 0 <= newW < len(T) and 0 <= newK < len(T):
        if T[newW][newK] == 0:
            return newW, newK
    return -1, -1


def rekurencja(T, k, w = 0, moves = 0) -> int:
    if w == len(T) - 1:
        return moves

    current_result = float('inf')
    for i in range(4):
        nowe_wspolrzedne = isPossible(T, w, k, i)
        if nowe_wspolrzedne[0] != -1:
            wynik = rekurencja(T, nowe_wspolrzedne[1], nowe_wspolrzedne[0], moves + 1)
            current_result = min(current_result, wynik)

    return current_result


def main_function(T) -> int:
    final_result = float('inf')

    for i in range(len(T[0])):
        if T[0][i] == 0:
            result = rekurencja(T, i)
            final_result = min(final_result, result)
    if final_result == float('inf'):
        return -1
    return final_result


# N = int(input("N: "))
# T = [[randint(0, 1) for _ in range(N)] for _ in range(N)]
# print(main_function(T))


# --- Tutaj wklej swoje funkcje: rekurencje i main (zakładam, że main nazywa się `skoczek`) ---
# Jeśli Twoja funkcja nazywa się inaczej, zmień nazwę w linijce `wynik = ...` poniżej.

def testuj(nazwa, T, oczekiwany_wynik):
    print(f"--- TEST: {nazwa} ---")
    try:
        # ZMIEŃ 'skoczek(T)' NA NAZWĘ SWOJEJ GŁÓWNEJ FUNKCJI
        wynik = main_function(T)

        if wynik == oczekiwany_wynik:
            print(f"✅ SUKCES! Wynik: {wynik}")
        else:
            print(f"❌ BŁĄD. Otrzymano: {wynik}, Oczekiwano: {oczekiwany_wynik}")
    except Exception as e:
        print(f"❌ WYJĄTEK (Błąd w kodzie): {e}")
    print("-" * 20)


# ==========================================
# PRZYKŁADY TESTOWE
# ==========================================

T1 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
testuj("Szybki strzał (3x3)", T1, 1)

T2 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 1]
]
testuj("Ściana na mecie", T2, -1)  # Lub inf, zależy jak zwracasz błąd

T3 = [
    [0, 1, 1, 1],  # Start tylko z (0,0)
    [1, 1, 1, 1],  # Rząd 1 zablokowany (nie da się tu wylądować)
    [1, 0, 1, 1],  # Lądowanie możliwe tylko na (2,1)
    [1, 1, 1, 0]  # Meta tylko w (3,3)
]
testuj("Slalom (4x4)", T3, 2)

T4 = [
    [0, 1, 1, 1, 0],  # Dwa starty: (0,0) i (0,4)
    [1, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],  # Lądowiska
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 0]  # Mety
]
testuj("Dwie drogi (krótka i długa)", T4, 2)
