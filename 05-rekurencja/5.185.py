"""
Dane jest N szkatułek, każda mogąca pomieścić maksymalnie 20 sztabek złota. Możemy
przenosić sztabki złota pomiędzy szkatułkami, jednak liczba sztabek w żadnej szkatułce nie może zmienić
się o więcej niż 2 sztabki. Dana jest tablica T[N] zawierająca liczby sztabek w poszczególnych szkatułkach.
Proszę napisać funkcję gold(T), która sprawdza, czy jest możliwe takie przeniesienie części sztabek pomię-
dzy szkatułkami, tak aby w liczba sztabek w każdej szkatułce była liczbą pierwszą. Funkcja powinna zwrócić
wartość True albo False.
Przykłady:
gold([4, 18, 15, 14, 14, 6]) powinna zwrócić True, nowe wartości [2, 19, 17, 13, 13, 7],
gold([3, 10, 11, 18, 16, 16]) powinna zwrócić False
"""


def isPrime(n):
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


def recurencion(T, pattern, indeks = 0, current = 0):
    if indeks == len(T):
        return current == pattern
    for number in T[indeks]:
        if recurencion(T, pattern, indeks + 1, current + number):
            return True
    return False


def gold(T):
    extents = []

    for element in T:
        tablica = []
        for number in range(element - 2, element + 3):
            if isPrime(number):
                tablica.append(number)
        if tablica == []:
            return False
        extents.append(tablica)
    return recurencion(extents, sum(T))


print(gold([4, 18, 15, 14, 14, 6]))
print(gold([3, 10, 11, 18, 16, 16]))
