"""
Dany jest ciąg określony wzorem: An+1 = (An mod2) *(3 *An + 1) + (1−An mod2) *An/2
Startując z dowolnej liczby naturalnej >1 ciąg ten osiąga wartość 1. Proszę napisać program, który znajdzie
wyraz początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.
"""
max_licznik = 0
a1 = 0
for i in range(2, 10000):
    licznik = 0
    an = i
    while an != 1:
        an = (an % 2) * (3 * an + 1) + (1 - an % 2) * an / 2
        licznik += 1
    if licznik > max_licznik:
        max_licznik = licznik
        a1 = i

print(max_licznik, a1)
