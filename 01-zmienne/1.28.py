"""
Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.
"""


def czy_palindrom_dziesietny(n):
    if n < 0: return False

    odwrocona = 0
    temp = n

    while temp > 0:
        odwrocona = odwrocona * 10 + temp % 10
        temp //= 10

    return n == odwrocona


def czy_palindrom_dwojkowy(n):
    if n < 0: return False

    odwrocona_bin = 0
    temp = n

    while temp > 0:
        print(odwrocona_bin)
        bit = temp % 2
        odwrocona_bin = odwrocona_bin * 2 + bit
        temp //= 2

    print(n,odwrocona_bin)
    return n == odwrocona_bin


n = int(input("Podaj liczbę: "))

if czy_palindrom_dziesietny(n):
    print(f"Liczba {n} JEST palindromem dziesiętnym.")
else:
    print(f"Liczba {n} NIE JEST palindromem dziesiętnym.")

if czy_palindrom_dwojkowy(n):
    print(f"Liczba {n} JEST palindromem dwójkowym.")
else:
    print(f"Liczba {n} NIE JEST palindromem dwójkowym.")

