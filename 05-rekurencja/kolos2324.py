"""
Na liczbach naturalnych możemy wykonywać następujące operacje:
1. 𝐴(𝑛) zamienia liczbę 𝑛 na sumę jej podzielników właściwych (mniejszych od samej liczby), np.
𝐴(1) = 1, 𝐴(6) = 6, 𝐴(12) = 16, 𝐴(17) = 1.
2. 𝐵(𝑛) zamienia liczbę 𝑛 na najmniejszy, większy od tej liczby wyraz ciągu Fibonacciego, np.
𝐵(1) = 2, 𝐵(4) = 5, 𝐵(8) = 13.
3. 𝐶(𝑛) zwiększa liczbę 𝑛 o liczbę będącą rewersem liczby 𝑛, np. 𝐶(1) = 2, 𝐶(10) = 11, 𝐶(13) = 44
Proszę napisać funkcję cycle(x,n), która sprawdza czy startując od liczby 𝑥 możemy do niej powrócić
wykonując sekwencję operacji spośród A,B,C o długości większej od 1 i nie większej od n. Jeżeli jest to
możliwe, funkcja powinna zwrócić długość znalezionej sekwencji operacji, w przeciwnym wypadku
należy zwrócić wartość 0.
Na przykład wywołanie:
cycle(29,6) powinno zwrócić 4 (cykl 29, B, 55, B, 89, C, 187, A, 29), [przykład jest błędny, 𝐵(29) = 34]
cycle(31,6) powinno zwrócić 0
"""
from math import isqrt


def operationA(n):
    if n == 1:
        return 1
    suma = 0
    for number in range(1, isqrt(n) + 1):
        if n % number == 0:
            suma += number
            new = n // number
            if new != number and new < n:
                suma += new
    return suma


def operationB(n):
    a = 0
    b = 1
    while a <= n:
        a, b = b, a + b
    return a


def operationC(n):
    suma = n
    number = 0
    while n > 0:
        number = number * 10 + (n % 10)
        n //= 10
    suma += number
    return suma


def cycle(x, n, start, result = 0):
    if result > n:
        return float('inf')

    if x == start and result > 1:
        return result

    results = []
    wynikA = cycle(operationA(x), n, start, result + 1)
    if wynikA != float('inf'):  results.append(wynikA)
    wynikB = cycle(operationB(x), n, start, result + 1)
    if wynikB != float('inf'):  results.append(wynikB)
    wynikC = cycle(operationC(x), n, start, result + 1)
    if wynikC != float('inf'):  results.append(wynikC)

    if not results:
        return float('inf')
    return min(results)

def main_function(x,n):
    wynik = cycle(x,n,x)
    if wynik == float('inf'):
        return 0
    return wynik


print(f"Dla x=29, n=6: {main_function(29, 6)}") # Powinno być 4
print(f"Dla x=31, n=6: {main_function(31, 6)}") # Powinno być 0

