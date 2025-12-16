"""
Dane są trzy operacje: A,B,C przekształcające liczbę naturalną x na inną liczbę naturalną.
• A zamienia liczbę x na jej rewers i dodaje 1. Na przykład: 123→322, 230 →33.
• B zamienia liczbę x na najmniejszą liczbę pierwszą większą od x. Na przykład 13→17, 20 →23.
• C oblicza odwrotność liczby x i zwraca liczbę złożoną z 3 cyfr rozwinięcia dziesiętnego odwrotności, po
pominięciu początkowych zer. Na przykład: 6→166 bo 1/6 = 0.16666..., 10 →100 bo 1/10 = 0.1000...,
12 →833 bo 1/12 = 0.083333..., 997 →100 bo 1/997 = 0.001003009...
Proszę napisać funkcję cykl(x), która dla liczby naturalnej x zwraca minimalną sekwencję operacji, których
wykonanie powraca do liczby początkowej x. Do funkcji należy przekazać wyłącznie wartość początkową x,
funkcja powinna zwrócić napis złożony z liter A,B,C. Jeżeli nie jest możliwy powrót do wartości początkowej
w mniej niż 10 operacjach, funkcja powinna zwrócić napis pusty. Można założyć, że x <= 10^6

Przykłady:
cykl(3)="BCA", 3 →5 →200 →3,
cykl(35)="BBBA", 35 →37 →41 →43 →35,
cykl(45)="CABCA", 45 →222 →223 →227 →440 →45,
cykl(51)="", cykl krótszy niż 10 nie istnieje
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


def operation_A(n):
    result = 0
    while n > 0:
        result = result * 10 + (n % 10)
        n //= 10
    return result + 1


def operation_B(n):
    number = n + 1
    while True:
        if isPrime(number):
            return number
        number += 1


def operation_C(n):
    if n == 0:
        return 0
    licznik = 1
    while licznik < n:
        licznik *= 10
    wynik = 0
    for _ in range(3):
        cyfra = licznik // n
        wynik = wynik * 10 + cyfra
        licznik = (licznik % n) * 10
    return wynik


def cykl(n, original, result = ""):
    if len(result) >= 10:
        return ""

    if n == original and len(result) > 0:
        return result

    results = []
    wynik_A = cykl(operation_A(n),original,result+"A")
    if wynik_A: results.append(wynik_A)
    wynik_B = cykl(operation_B(n),original,result+"B")
    if wynik_B: results.append(wynik_B)
    wynik_C = cykl(operation_C(n),original,result+"C")
    if wynik_C: results.append(wynik_C)
    if not results:
        return ""

    return min(results,key = len)


n = int(input("n: "))
wynik = cykl(n, n)
print(wynik)
