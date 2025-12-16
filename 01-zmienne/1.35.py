"""
Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
ta zawiera cyfrę równą liczbie swoich cyfr.
"""


def liczba_cyfr(n):
    if n == 0:
        return 1

    licznik = 0
    while n > 0:
        n //= 10
        licznik += 1

    return licznik


def funkcja(n, ile):
    while n > 0:
        if n % 10 == ile:
            return True
        n //= 10
    return False


n = int(input("n: "))
ilosc_cyfr = liczba_cyfr(n)
print(funkcja(n, ilosc_cyfr))
