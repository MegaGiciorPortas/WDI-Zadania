"""
Napisać program, który wyznacza ostatnia niezerową cyfrę liczby N!. Program powinien
działać dla N rzędu 10^100.

"""


def ilosc_czynnika(n, czynnik):
    suma = 0
    while n >= czynnik:
        suma += n // czynnik
        n //= czynnik
    return suma


def cykl_dwojek(n):
    wskaznik = n % 4
    if wskaznik == 0:
        return 6
    elif wskaznik == 1:
        return 2
    elif wskaznik == 2:
        return 4
    return 8


def cykl_reszty_liczb(n):
    liczba_cykli = n // 10
    if liczba_cykli % 2 == 0:
        ostatnia = 1
    else:
        ostatnia = 9

    start = liczba_cykli * 10 + 1
    for i in range(start, n + 1):
        last_digit = i % 10
        if not last_digit % 2 == 0 and not last_digit % 5 == 0:
            ostatnia = (ostatnia * last_digit) % 10

    return ostatnia


n = int(input("n: "))
if n == 1 or n == 0:
    print(1)
else:
    liczba_dwojek = ilosc_czynnika(n, 2)
    liczba_piatek = ilosc_czynnika(n, 5)
    dwojki_do_uzycia = liczba_dwojek - liczba_piatek

    ostatnia_cyfra_dwojek = cykl_dwojek(dwojki_do_uzycia)
    ostatnia_cyfra_reszta = cykl_reszty_liczb(n)

    ostatnia_cyfra_wynik = (ostatnia_cyfra_dwojek * ostatnia_cyfra_reszta) % 10
    print(ostatnia_cyfra_wynik)
