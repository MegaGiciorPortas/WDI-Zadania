"""
Proszę napisać program, który wypełnia N-elementową tablicę T trzycyfrowymi liczba-
mi pseudolosowymi, a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego znajdujące-
go się w tablicy dla którego w tablicy występuje również rewers tego ciągu. Na przykład dla tablicy: t=
[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzią jest liczba 4.
"""

from random import randint


def func(T):
    N = len(T)

    # 1. POPRAWKA PĘTLI:
    # Iterujemy po 'L' (długość), od N (cała tablica) do 1.
    for L in range(N, 0, -1):

        # Iterujemy 'i' (start pierwszego fragmentu)
        for i in range(N - L + 1):

            fragment1 = T[i: i + L]
            fragment1_rewers = fragment1[::-1]  # Robimy rewers (w C++ pętlą)

            # Iterujemy 'j' (start drugiego fragmentu)
            for j in range(N - L + 1):

                # 2. POPRAWKA "SAMODOPASOWANIA":
                # Pomiń, jeśli sprawdzamy ten sam fragment
                if i == j:
                    continue

                fragment2 = T[j: j + L]

                if fragment1_rewers == fragment2:
                    # Znaleźliśmy! Ponieważ idziemy od L=N w dół,
                    # to jest to najdłuższy możliwy.
                    return L

    # 3. POPRAWKA ZWROTU:
    # Jeśli pętle się skończyły, nic nie znaleziono
    return 0


N = int(input("N: "))
T = [randint(100, 999) for _ in range(N)]
print(func(T))
