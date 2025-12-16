"""
Zadanie 55. Proszę napisać program wczytujący dwie liczby naturalne a,b i wypisujący rozwinięcie dzie-
siętne ułamka a/b uwzględniając ułamki okresowe. Na przykład 2/3 = 0.(6),1/5 = 0.2,1/6 = 0.1(6),1/7 =
0.(142857)
"""


def main():
    a = int(input("a: "))
    b = int(input("b: "))
    wynik = ""

    if b == 0:
        print("Błąd: Dzielenie przez zero.")
        return None

    # 1. Oblicz i wypisz część całkowitą
    wynik += str(a // b)
    wynik += "."

    # 2. Oblicz pierwszą resztę
    reszta = a % b

    if reszta == 0:
        wynik += "0"
        return wynik

    # --- Używamy algorytmu Floyda (Żółw i Zając) do wykrycia cyklu ---
    # Musimy znaleźć cykl LUB wykryć, że ułamek się kończy (reszta == 0)

    # Inicjalizujemy obie zmienne w tym samym punkcie (pierwsza reszta)
    zolw = reszta
    zajac = reszta

    # Musimy wykonać pętlę "do-while"
    # Najpierw wykonujemy jeden krok, zanim sprawdzimy warunek
    while True:
        # Żółw przesuwa się o 1 krok:
        zolw = (zolw * 10) % b

        # Zając przesuwa się o 2 kroki:
        zajac = (zajac * 10) % b
        zajac = (zajac * 10) % b

        # Jeśli zając trafił na 0, ułamek się kończy (np. 1/4)
        if zajac == 0:
            # Nie ma cyklu. Wypisz resztę normalnie.
            # Zaczynamy od nowa od pierwszej reszty
            temp_r = reszta
            while temp_r > 0:
                # Oblicz następną cyfrę
                temp_r = temp_r * 10
                wynik += str(temp_r // b)
                # Oblicz następną resztę
                temp_r = temp_r % b
            return wynik

        # Jeśli żółw i zając się spotkały, znaleźliśmy cykl
        if zolw == zajac:
            break

    # --- Jeśli dotarliśmy tutaj, wiemy na 100%, że jest cykl ---
    # Teraz musimy znaleźć, GDZIE on się zaczyna.

    # 1. Resetujemy żółwia na pozycję startową (pierwsza reszta)
    zolw = reszta

    # 2. Przesuwamy żółwia i zająca o JEDEN krok na raz,
    #    aż znowu się spotkają. Miejsce spotkania to POCZĄTEK cyklu.
    while zolw != zajac:
        zolw = (zolw * 10) % b
        zajac = (zajac * 10) % b

    # Zmienna 'zolw' (lub 'zajac') przechowuje teraz resztę,
    # od której zaczyna się cykl (np. 4 dla 1/6)
    poczatek_cyklu_reszta = zolw

    # --- Mamy już wszystko. Drukujemy wynik w dwóch fazach ---

    # Faza 1: Drukuj "część nienokresową" (stem)
    # Zaczynamy od nowa i drukujemy cyfry, AŻ dojdziemy do reszty
    # rozpoczynającej cykl.
    temp_r = reszta
    while temp_r != poczatek_cyklu_reszta:
        temp_r = temp_r * 10
        wynik += str(temp_r // b)
        temp_r = temp_r % b

    # Faza 2: Drukuj "część okresową" (cykl)
    wynik += "("

    # Zaczynamy od pierwszej reszty cyklu
    temp_r = poczatek_cyklu_reszta
    while True:
        temp_r = temp_r * 10
        wynik += str(temp_r // b)
        temp_r = temp_r % b

        # Drukujemy, aż wrócimy do początku cyklu
        if temp_r == poczatek_cyklu_reszta:
            break

    wynik += ")"
    return wynik

print(main())
