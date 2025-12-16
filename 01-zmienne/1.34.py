"""
Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy jej
cyfry stanowia ciag geomtetryczny
"""


def czy_geometryczny(n):
    if n < 100:
        return True

    a1 = n % 10
    n //= 10
    a2 = n % 10
    n //= 10

    while n > 0:
        a3 = n % 10
        n //= 10
        if a1 * a3 != a2 * a2:
            return False
        a1 = a2
        a2 = a3
    return True


n = int(input("n: "))
print(czy_geometryczny(n))
