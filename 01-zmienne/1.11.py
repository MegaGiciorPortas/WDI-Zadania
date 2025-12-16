"""
Proszę napisać program sprawdzający czy zadana liczba jest pierwszą.
"""

def czy_pierwsza(n):
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4

    return True


n = int(input("n: "))
print(czy_pierwsza(n))
