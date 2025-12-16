"""
Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę skład-
ników. Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2
"""


def podzial(n, last = 1, result = "") -> None:
    if n == 0:
        if result.find("+") != result.rfind("+"):
            print(result[:-1])
        return

    for liczba in range(last, n + 1):
        print(n,liczba)
        podzial(n - liczba, liczba, result + f"{liczba}+")


podzial(4)
