"""
Mając daną dodatnią liczbę całkowitą N , stwórzmy nową liczbę dodając kwadraty cyfr
liczby N . Można udowodnić, że postępując w ten sposób wielokrotnie otrzymamy w końcu wynik 1 lub 4.
Przykład: 13 = 12 + 32 = 1 + 9 = 10 (Krok 1) 10 = 12 + 02 = 1 + 0 = 1 (Krok 2, kończymy iterację ponieważ
uzyskaliśmy liczbę 1) Jeżeli w opisanej powyżej procedurze uzyskamy wynik 1, to liczbę N nazywamy “jedno-
kwadratową”. Proszę napisać program, który znajduje K-tą liczbę w zadanym przedziale [L, U ], która jest
jednocześnie jednokwadratowa i pierwsza.
"""


def czy_pierwsza(n):
    if n <= 1:
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


def czy_jednokwadratowa(n):
    liczba = n
    suma = 0
    while True:
        while liczba > 0:
            suma += (liczba % 10) ** 2
            liczba //= 10
        if suma == 4:
            return False
        if suma == 1:
            return True
        liczba = suma
        suma = 0


L = int(input("L: "))
U = int(input("U: "))
K = int(input("K: "))

licznik = 0
for i in range(L, U + 1):
    if czy_pierwsza(i) and czy_jednokwadratowa(i):
        licznik += 1
        if licznik == K:
            print(i)
            break
