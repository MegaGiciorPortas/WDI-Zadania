"""
Dana jest tablica T[N] wypełniona niepowtarzającymi się liczbami naturalnymi. Proszę
napisać funkcję trojki(T) która zlicza wszystkie trójki liczb, które spełniają następujące warunki:
(1) największym wspólnym dzielnikiem trzech liczb jest liczba 1,
(2) pomiędzy dwoma kolejnymi elementami trójki może być co najwyżej jedna przerwa.
Funkcja powinna zwrócić liczbę znalezionych trójek.
Przykładowe wywołania funkcji:
print(trojki([2,4,6,7,8,10,12])) # 0 trójek
print(trojki([2,3,4,6,7,8,10])) # 1 trójka (3,4,7)
print(trojki([2,4,3,6,5])) # 2 trójki (2,3,5),(4,3,5)
print(trojki([2,3,4,5,6,8,7])) # 5 trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)
"""


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def trojki(T):
    N = len(T)
    liczba_trojek = 0

    for i in range(N):
        for j in range(i + 1, min(i + 3, N)):
            for k in range(j + 1, min(j + 3, N)):
                if nwd(nwd(T[i],T[j]),T[k]) == 1:
                    liczba_trojek += 1

    return liczba_trojek


print(trojki([2, 4, 6, 7, 8, 10, 12]))  # 0 trójek
print(trojki([2, 3, 4, 6, 7, 8, 10]))  # 1 trójka (3,4,7)
print(trojki([2, 4, 3, 6, 5]))  # 2 trójki (2,3,5),(4,3,5)
print(trojki([2, 3, 4, 5, 6, 8, 7]))  # 5 trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)
