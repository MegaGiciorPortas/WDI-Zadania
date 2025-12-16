"""
Proszę znaleźć wyrazy początkowe ciągu zamiast 1,1 o najmniejszej sumie, aby w ciągu
analogicznym do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.
"""

najmniejsza_suma = 2026
najmniejsze_a = 0
najmniejsze_b = 0
for a in range(2, 2025):
    for b in range(2, 2025):
        if a == 1 and b == 1:
            continue

        a1 = a
        a2 = b
        while a2 < 2025:
            a1, a2 = a2, a1 + a2

        if a2 == 2025:
            if a + b < najmniejsza_suma:
                najmniejsze_a = a
                najmniejsze_b = b
                najmniejsza_suma = a + b

print(najmniejsze_a, najmniejsze_b, najmniejsza_suma)
