"""
Kwadrat jest opisywany czwórką liczb całkowitych (x1,x2,y1,y2), gdzie x1,x2,y1,y2 ozna-
czają proste ograniczające kwadrat x1 <x2, y1 <y2. Dana jest tablica T zawierająca opisy N kwadratów.
Proszę napisać funkcję, która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć 13 nienacho-
dzących na siebie kwadratów, których suma pól jest równa 2012 i False w przeciwnym przypadku
"""


def obliczanie_pola(T):
    return abs(T[1] - T[0]) * abs(T[3] - T[2])


def czy_nachodza_na_siebie(T1, T2) -> bool:
    # T = [x1,x2,y1,y2]
    return T1[1] <= T2[0] or T2[1] <= T1[0] or T1[3] <= T2[2] or T2[3] <= T1[2]


def rekurencja(T, usedSquares, used, start, counter, currentSum) -> bool:
    N = len(T)

    if counter == 13:
        return currentSum == 2012

    for i in range(start + 1, N):
        if usedSquares[i] == 0:
            flaga = True
            for element in used:
                if not czy_nachodza_na_siebie(element, T[i]):
                    flaga = False
                    break
            if flaga:
                usedSquares[i] = 1
                used.append(T[i])
                if rekurencja(T, usedSquares, used, i, counter + 1, currentSum + obliczanie_pola(T[i])):
                    return True
                usedSquares[i] = 0
                used.pop()
    return False


def main_function(T) -> bool:
    N = len(T)
    usedSquares = [0 for _ in range(N)]

    used = []
    for i in range(N):
        usedSquares[i] = 1
        used.append(T[i])
        if rekurencja(T, usedSquares, used, i, 1, obliczanie_pola(T[i])):
            return True
        usedSquares[i] = 0
        used.pop()

    return False


# --- Tutaj Twoja funkcja solve/wrapper (nazwij ją 'zadanie_kwadraty' lub zmień wywołanie w testach) ---
# def zadanie_kwadraty(T): ...

def testuj(nazwa, T, oczekiwany_wynik):
    print(f"--- TEST: {nazwa} ---")
    try:
        wynik = main_function(T)
        if wynik == oczekiwany_wynik:
            print(f"✅ SUKCES! Wynik: {wynik}")
        else:
            print(f"❌ BŁĄD. Otrzymano: {wynik}, Oczekiwano: {oczekiwany_wynik}")
    except Exception as e:
        print(f"❌ WYJĄTEK: {e}")
    print("-" * 30)


# POMOCNIK: Tworzenie kwadratu (x, x+bok, y, y+bok)
def sq(x, y, bok):
    return [x, x + bok, y, y + bok]


# ==========================================
# SCENARIUSZE TESTOWE
# ==========================================

T1 = []
x_pos = 0
# 11 sztuk 13x13
for _ in range(11):
    T1.append(sq(x_pos, 0, 13))
    x_pos += 20
# 1 sztuka 12x12
T1.append(sq(x_pos, 0, 12))
x_pos += 20
# 1 sztuka 3x3
T1.append(sq(x_pos, 0, 3))

# Dodajemy "śmieci" (kwadraty, których nie należy wybierać)
T1.append(sq(1000, 1000, 50))  # Za duży
T1.append(sq(2000, 2000, 1))  # Za mały

testuj("Idealny zestaw (13 sztuk, suma 2012)", T1, True)

T2 = []
x_pos = 0
for _ in range(11):
    T2.append(sq(x_pos, 0, 13))
    x_pos += 20
T2.append(sq(x_pos, 0, 12))
x_pos += 20
T2.append(sq(x_pos, 0, 2))  # <--- ZMIANA (2x2 zamiast 3x3)

testuj("Zła suma (Suma 2007)", T2, False)

T3 = []
x_pos = 0
for _ in range(10):  # Tylko 10 sztuk 13x13
    T3.append(sq(x_pos, 0, 13))
    x_pos += 20

T3.append(sq(x_pos, 0, 12))  # Oryginalna 12-tka
x_pos += 20
T3.append(sq(x_pos, 0, 3))  # Oryginalna 3-ka
x_pos += 20

# Te dwa zastępują jeden 13x13
T3.append(sq(x_pos, 0, 12))
x_pos += 20
T3.append(sq(x_pos, 0, 5))

testuj("Zła liczebność (14 sztuk zamiast 13)", T3, False)

T4 = []
# Pierwszy kwadrat (13x13) w punkcie (0,0)
T4.append(sq(0, 0, 13))

# Drugi kwadrat (13x13) TEŻ w punkcie (0,0) - KOLIZJA!
T4.append(sq(0, 0, 13))

# Reszta (9 sztuk 13x13 + 12x12 + 3x3) przesunięta dalej
x_pos = 20
for _ in range(9):
    T4.append(sq(x_pos, 0, 13))
    x_pos += 20
T4.append(sq(x_pos, 0, 12))
x_pos += 20
T4.append(sq(x_pos, 0, 3))

testuj("Kolizja geometryczna", T4, False)
