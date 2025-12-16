"""
Napisać program, który wyznacza liczbę zer jakimi kończy się liczba N! Program powinien
liczyć liczby dla rzędu N = 10 ^ 100

liczba_Zer = 1/5 + 1/25 + 1/125
"""

n = int(input("n: "))
zera = 0
licznik = 1
while True:
    if 5 ** licznik > n:
        break
    zera += n // (5 ** licznik)
    licznik += 1

print(zera)
