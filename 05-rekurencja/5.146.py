"""
”Waga” liczby jest określona jako liczba różnych czynników pierwszych liczby. Na przykład
waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.
"""


def waga(n) -> int:
    i = 2
    w = 0
    while i * i <= n:
        if n % i == 0:
            w += 1
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        w += 1
    return w


def podzial(T, p = 0, s1 = 0, s2 = 0, s3 = 0) -> bool:
    N = len(T)
    if p == N:
        return s1 == s2 == s3

    return podzial(T, p + 1, s1 + T[p], s2, s3) or podzial(T, p + 1, s1, s2 + T[p], s3) or podzial(T, p + 1, s1, s2,
                                                                                                   s3 + T[p])


def function(T) -> bool:
    N = len(T)
    Wagi = [waga(T[i]) for i in range(N)]

    if sum(Wagi) % 3 != 0:  return False

    return podzial(T)


T = [3, 2, 2, 2, 2, 2]
print(function(T))
