"""
Dana jest liczba naturalna N. Proszę napisać funkcję, która zwróci maksymalną długość
powtarzającej się sekwencji cyfr w tej liczbie. Jeżeli w liczbie nic się nie powtarza zwracamy 0.
Przykłady powtarzających się sekwencji: 2024 powtarza się 2, zwracamy 1, 123456 nic się nie powtarza,
zwracamy 0, 1234568234 powtarza się 234, zwracamy 3, 2222222200 najdłuższa powtarzająca się sekwencja
to 2222, zwracamy 4.
"""


def funkcja(napis):
    maksymalna_dlugosc = 0
    for poczatek in range(len(napis)):
        for koniec in range(poczatek + 1, len(napis) + 1):
            fragment = napis[poczatek:koniec]
            if fragment in napis[koniec:]:
                if len(fragment) > maksymalna_dlugosc:
                    maksymalna_dlugosc = len(fragment)

    return maksymalna_dlugosc


N = int(input("N: "))
napis = str(N)

print(funkcja(napis))
