"""
Zadanie 145
Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej cyfry.
"""


def isPrime(n):
    n = int(n)
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def function(k, a = "", oryginal = ""):
    if oryginal == "":
        oryginal = k
    if k == "":
        if len(a) > 1 and a != oryginal:
            if isPrime(int(a)):
                print(a)
        return None
    function(k[1:], a, oryginal)
    function(k[1:], a + k[0], oryginal)


k = input("k: ")
function(k)
