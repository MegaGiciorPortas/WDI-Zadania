"""
Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpo-
wiada na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą.
Długość każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla
ciągu 110100 nie jest możliwe
"""
from random import randint


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


def decimal(s):
    result = 0
    escalating = len(s) - 1
    for char in s:
        result += 2 ** escalating * int(char)
        escalating -= 1
    return result


def function(T, indeks = 0, number = "", orginal = ""):
    if orginal == "":
        for char in T:
            orginal += str(char)

    if indeks == len(T):
        if number == orginal:
            return False
        if isPrime(decimal(number)):
            return True
        return False

    if isPrime(decimal(number)):
        if function(T, indeks + 1, "", orginal):
            return True
    if len(number) <= 29:
        return function(T, indeks + 1, number + str(T[indeks]), orginal)
    return False


N = int(input("N: "))
T = [randint(0, 1) for _ in range(N)]
print(function(T))
