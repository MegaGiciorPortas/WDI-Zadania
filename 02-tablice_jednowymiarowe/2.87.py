"""
Napis nazywamy wielokrotnym, jeżeli powstał przez n-krotne (n>1) powtórzenie innego
napisu o długości co najmniej 1. Przykłady napisów wielokrotnych: ABCABCABC, AAAA, ABAABA.
Dana jest tablica T[N] zawierająca napisy. Proszę napisać funkcję multi(T), która zwraca długość najdłuż-
szego napisu wielokrotnego występującego w tablicy T lub wartość 0, jeżeli takiego napisu nie ma w tablicy.
"""


def najwiekszy_dzielnik_mniejszy_od_niej_samej(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return n // i
        i += 1
    return 1


def porownywanie_napisow(napis1, napis2):
    dlugosc_napis2 = len(napis2)
    for i in range(len(napis1)):
        if napis1[i] != napis2[i % dlugosc_napis2]:
            return False
    return True


def sprawdzanie_napisu(napis):
    dlugosc_napisu = len(napis)
    meta = najwiekszy_dzielnik_mniejszy_od_niej_samej(dlugosc_napisu)
    for i in range(meta):
        fragment = napis[:i + 1]

        if porownywanie_napisow(napis, fragment):
            return True
    return False


def multi(T):
    najdluzszy_napis = 0

    for napis in T:
        if sprawdzanie_napisu(napis):
            if len(napis) > najdluzszy_napis:
                najdluzszy_napis = len(napis)

    return najdluzszy_napis


T = [
    "ABCABCABC",  # 0: Dł. 9. Wielokrotny (baza: "ABC", n=3)
    "KOTKOT",  # 1: Dł. 6. Wielokrotny (baza: "KOT", n=2)
    "TEST",  # 2: Dł. 4. NIE jest wielokrotny.
    "ABABAB",  # 3: Dł. 6. Wielokrotny (baza: "AB", n=3)
    "AAAAA",  # 4: Dł. 5. Wielokrotny (baza: "A", n=5)
    "ABCABCA",  # 5: Dł. 7. NIE jest wielokrotny (pułapka).
    "XYZ",  # 6: Dł. 3. NIE jest wielokrotny (n=1).
    ""  # 7: Dł. 0. NIE jest wielokrotny.
]

T1 = [
    "BardzoDlugiNapisAleNieWielokrotny",  # Dł. 34. NIE.
    "abcabcabd",  # Dł. 9.  NIE (pułapka, ostatnia litera inna).
    "KOKOKO",  # Dł. 6.  TAK (Baza: "KO", n=3)
    "ALALA",  # Dł. 5.  NIE (pułapka, nie da się podzielić).
    "123123123",  # Dł. 9.  TAK (Baza: "123", n=3)
    "X"  # Dł. 1.  NIE (n=1).
]

T2 = [
    "ABAB",  # Dł. 4. TAK (Baza: "AB", n=2)
    "ABC",  # Dł. 3. NIE (n=1)
    "AAAAAAAA",  # Dł. 8. TAK (np. Baza: "AA", n=4)
    "ABC ABC"  # Dł. 7. NIE (spacja to też znak).
]

print(multi(T))
print(multi(T1))
print(multi(T2))
