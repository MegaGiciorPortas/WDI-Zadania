"""
Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu
Fibonacciego, np. 9,14,15,17,22. Proszę napisać program, który wczytuje liczbę naturalną n, wylicza i
wypisuje następną taką liczbę większą od n. Można założyć, że 0 <n<1000.
"""

def tablica_Fibonacci(n):
    tablica = [0, 1]
    a1 = 1
    a2 = 1
    while a2 <= n:
        a1, a2 = a2, a1 + a2
        tablica.append(a1)
    print(tablica)
    return tablica


def funkcja(n, tablica):
    lewy = 0
    suma = 0
    for prawy in range(len(tablica)):
        suma += tablica[prawy]

        while suma > n:
            suma -= tablica[lewy]
            lewy += 1

        if suma == n:
            return True

    return False


n = int(input("n: "))
liczby_Fibonacciego = tablica_Fibonacci(n)
print(funkcja(n,liczby_Fibonacciego))