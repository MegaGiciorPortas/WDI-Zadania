"""
Proszę napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych
wyrazów ciągu Fibonacciego. Wyznaczyć te ilorazy dla różnych wartości dwóch początkowych wyrazów
ciągu.
"""


def znajdz_granice_dla_pary(a, b):
    f1 = a
    f2 = b

    if f1 == 0 and f2 == 0:
        return 0.0

    while f2 <= 1e7:
        f1, f2 = f2, f1 + f2

    if f1 == 0:
        return 0.0

    return f2 / f1


print("Badanie granicy ilorazu F(n+1) / F(n) dla różnych par startowych:")

pary_do_testow = [
    (1, 1),
    (1, 2),
    (5, 8),
    (10, 3),
    (123, 456)
]

for para in pary_do_testow:
    a = para[0]
    b = para[1]

    granica = znajdz_granice_dla_pary(a, b)

    print(f"Para startowa: ({a}, {b}) -> Granica ilorazu: {granica}")
