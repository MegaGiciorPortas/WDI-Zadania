'''
Napisać program, który wyznacza n-tą cyfrę po przecinku rozwinięcia dziesiętnego wartości
sqrt(2). Program powinien działać poprawnie dla n<100.

'''


def kwadrat(t):
    """
    Oblicza kwadrat liczby 't' (zapisanej jako tablica cyfr)
    i zwraca True, jeśli wynik jest >= 2.0
    """
    n = len(t)
    w = [0] * (2 * n)  # Tablica na wynik mnożenia

    # POPRAWKA 1: Pętle muszą być w zakresie (n), a nie (n+1)
    # To jest mnożenie "każdy z każdym" (jak w szkole)
    for i in range(n):
        for j in range(n):
            # Mnożymy cyfrę t[i] przez t[j] i dodajemy do odpowiedniego "słupka"
            # (i+j to pozycja dla ułamków 10^-(i+j))
            w[i + j] += t[i] * t[j]

    # Pętla obsługująca przeniesienia ("carry")
    # Idziemy od prawej do lewej (od końca tablicy)
    for i in range(2 * n - 1, 0, -1):
        # Przeniesienie (część dziesiętna) idzie w lewo
        w[i - 1] += w[i] // 10
        # Zostawiamy tylko cyfrę jedności
        w[i] = w[i] % 10

    # POPRAWKA 3: Sprawdzamy, czy "przestrzelił"
    # Czy część całkowita (w[0]) jest >= 2?
    if w[0] >= 2:
        return True
    else:
        return False


def zadanie(N):
    # Tablica na cyfry (1 przed przecinkiem, N po przecinku)
    t = [0] * (N + 1)
    t[0] = 1  # Zaczynamy od 1. ...

    # Pętla po kolejnych cyfrach (i = indeks cyfry do znalezienia)
    for i in range(1, N + 1):

        # POPRAWKA 2: Musimy sprawdzać cyfry od 0 do 9
        # Ale wiemy, że dla sqrt(2) żadna cyfra nie jest 0,
        # więc zaczniemy pętlę "digit" od 9 i pójdziemy w dół.
        # To jest bardziej wydajne (mniej wywołań 'kwadrat').

        for digit in range(9, -1, -1):  # Idziemy od 9 w dół do 0
            t[i] = digit  # Wstawiamy próbną cyfrę

            # Sprawdzamy, czy kwadrat JEST MNIEJSZY niż 2
            # (Odwróciliśmy logikę, aby pasowała do szukania od góry)
            if not kwadrat(t):
                # Jeśli [1, 4] (1.96) nie przestrzeliło,
                # to 4 jest dobrą cyfrą.
                # Przerywamy pętlę 'digit' i idziemy do 'i+1'.
                break

            # Jeśli 'kwadrat(t)' zwrócił True (np. dla 1.5 -> 2.25),
            # pętla 'digit' idzie dalej (próbuje 8, 7, ... aż do 4)

    return t[N]


N = int(input("N: "))
print(zadanie(N))