"""
Trójką prostokątny o bokach wyrażonych liczbami naturalnymi nazywamy Pitagorejskim.
Proszę napisać program poszukujący trójkątów Pitagorejskich w których długość przekątnej jest mniejsza
od liczby N wprowadzonej z klawiatury.
"""
from math import sqrt

n = int(input("n: "))
for c in range(n - 1, 4, -1):
    for a in range(1, c):
        for b in range(a, c):
            if a * a + b * b == c * c:
                print(a, b, c)

print("---------------")
for c in range(n - 1, 4, -1):
    for a in range(1, c):
        b_kwadrat = c * c - a * a
        b = int(sqrt(b_kwadrat))

        if b * b == b_kwadrat:
            print(a, b, c)
