"""
Napisać program, który wyznacza ostatnia niezerową cyfrę liczby N!. Program powinien
działać dla N rzędu 10^100.

"""


def liczba_czynnika(n, czynnik):
    suma = 0
    while n >= czynnik:
        suma += n // czynnik
        n //= czynnik
    return suma


def rozklad_na_czynniki(n):
    licznik = 2
    tablica = []
    while licznik * licznik <= n:
        while n % licznik == 0:
            tablica.append(licznik)
            n //= licznik
        licznik += 1

    if n > 1:
        tablica.append(n)

    return tablica


n = int(input("n: "))

liczba_czynnikow_2 = liczba_czynnika(n, 2)
liczba_czynnikow_5 = liczba_czynnika(n, 5)

ostatnia_cyfra = 1
for i in range(2, n + 1):
    czynniki = rozklad_na_czynniki(i)
    for x in czynniki:
        if x != 2 and x != 5:
            ostatnia_cyfra *= x
    ostatnia_cyfra = ostatnia_cyfra % 10

ilosc_uzytych_dwojek = liczba_czynnikow_2 - liczba_czynnikow_5
ostatnia_cyfra = (ostatnia_cyfra * (2 ** ilosc_uzytych_dwojek)) % 10
print(ostatnia_cyfra)
