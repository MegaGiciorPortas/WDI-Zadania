"""
Pewne liczby pierwsze są palindromami i pozostają liczbami pierwszymi pomimo pozbawiania
ich skrajnych cyfr. Na przykład: 71317→131 →3. Proszę napisać program, który wypisuje wszystkie takie
liczby mniejsze od N.
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


def czy_palindrom(n):
    kopia = n
    odwrocona = 0
    while kopia > 0:
        odwrocona = odwrocona * 10 + kopia % 10
        kopia //= 10
    return n == odwrocona


def okrajanie_liczb(n):
    if n // 100 == 0:
        return -1

    nowe_n = n // 10
    moc = 1
    temp = nowe_n
    while temp >= 10:
        temp //= 10
        moc *= 10

    return nowe_n % moc


n = int(input("n: "))
for i in range(1, n):
    a = i

    while True:
        if not czy_pierwsza(a) or not czy_palindrom(a):
            break

        a = okrajanie_liczb(a)

        if a == -1:
            print(i)
            break
