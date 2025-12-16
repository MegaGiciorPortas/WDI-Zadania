"""
Dany jest ciąg N liczb naturalnych, z którego wybieramy spójny fragment o długości K
(1 <K <N). Pomiędzy wszystkie elementy wybranego fragmentu możemy wstawiać operatory dodawania
albo mnożenia, tak aby powstało wyrażenie arytmetyczne. W powstałym wyrażeniu nie mogą wystąpić dwa
jednakowe operatory obok siebie. Interesuje nas znalezienie takiego fragmentu ciągu, który pozwala zbu-
dować wyrażenie o wartości będącej liczbą pierwszą. Proszę napisać funkcję find max(T), która dla ciągu
zawartego w tablicy T, wyznaczy wartość największej liczby pierwszej, jaką można znaleźć. Jeżeli taki pod-
ciąg nie istnieje, funkcja powinna zwrócić wartość zero.
Na przykład dla ciągu: 7,8,6,4,7,3 funkcja powinna zwrócić wartość 83
Możliwe podciągi dające liczby pierwsze to:
7 + 8 ∗6 + 4 = 59
7 + 8 ∗6 + 4 ∗7 = 83
6 ∗4 + 7 = 31
4 + 7 = 11
"""


def czy_pierwsza(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def obliczanie_wyrazenia_arytmetycznego(tablica):
    pierwsze_mnozenie = 0
    pierwsze_dodawanie = 0
    N = len(tablica)

    # 1 + 2 * 3 + 4 * 5 =
    # 1 * 2 + 3 * 4 + 5 =

    # pierwsze_mnozenie
    for i in range(0, N, 2):
        if i + 1 != N:
            pierwsze_mnozenie += tablica[i] * tablica[i + 1]
    if i != N:
        pierwsze_mnozenie += tablica[N - 1]

    # pierwsze_dodawanie
    pierwsze_dodawanie += tablica[0]
    for j in range(1, N, 2):
        if j + 1 != N:
            pierwsze_dodawanie += tablica[j] * tablica[j + 1]
    if j != N:
        pierwsze_dodawanie += tablica[N - 1]

    if not czy_pierwsza(pierwsze_dodawanie):
        pierwsze_dodawanie = 0
    if not czy_pierwsza(pierwsze_mnozenie):
        pierwsze_mnozenie = 0

    if pierwsze_mnozenie > pierwsze_dodawanie:
        return pierwsze_mnozenie
    return pierwsze_dodawanie


def find_max(T):
    maks_liczba = 0
    N = len(T)

    for poczatek in range(N - 1):
        for koniec in range(poczatek + 2, N + 1):
            if koniec - poczatek + 1 == N: continue
            podciag = T[poczatek:koniec]

            wartosc = obliczanie_wyrazenia_arytmetycznego(podciag)
            if wartosc > maks_liczba:
                maks_liczba = wartosc

    return maks_liczba


def find_max_v2(T):
    maks_liczba = 0
    N = len(T)

    for poczatek in range(N - 1):
        for koniec in range(poczatek + 2, N + 1):
            if koniec - poczatek + 1 == N:  continue

            suma_mnozenie = 0
            for k in range(poczatek, koniec - 1, 2):
                suma_mnozenie += T[k] * T[k + 1]
            if (koniec - poczatek) % 2 == 1:
                suma_mnozenie += T[koniec - 1]

            suma_dodawanie = T[poczatek]

            for k in range(poczatek + 1, koniec - 1, 2):
                suma_dodawanie += T[k] * T[k + 1]
            if (koniec - poczatek) % 2 == 0:
                suma_dodawanie += T[koniec - 1]


T = [7, 8, 6, 4, 7, 3]
print(find_max(T))
