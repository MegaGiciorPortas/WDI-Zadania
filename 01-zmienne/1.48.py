"""
Wybieramy dodatnią liczbę całkowitą X. Z liczby X wykreślamy ostatnią cyfrę. Postępu-
jemy tak, aż usuniemy wszystkie cyfry liczby X. Następnie sumujemy wszystkie powstałe w ten sposób liczby,
włączając liczbę X. Na przykład, jeżeli wybraliśmy X = 1234 to w kolejnych krokach otrzymamy odpowiednio
liczby 1234, 123, 12, 1. Ich suma to 1370. Mamy daną liczbę całkowitą dodatnią S. Proszę napisać program,
który znajduje liczbę X taką, że powyżej opisana procedura daje sumę S. Można pokazać, że dla dowolnej
dodatniej liczby S istnieje co najwyżej jedna taka wartość X. Jeżeli nie ma takiego X program powinien
wypisać -1.
"""


def zliczanie_powstalych_liczb(n):
    suma = n
    while n > 0:
        n //= 10
        suma += n
    return suma


def czy_istnieje_X(S):
    left = 0
    right = S

    while left <= right:
        mid = (left + right) // 2

        mid_suma = zliczanie_powstalych_liczb(mid)

        if mid_suma == S:
            return mid

        if mid_suma < S:
            left = mid + 1
        else:
            right = mid - 1
    return -1


S = int(input("S: "))
print(czy_istnieje_X(S))

