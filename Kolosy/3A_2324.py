"""
Dany jest ciąg 𝑁 liczb naturalnych, z których wybieramy spójny fragment o długości 𝐾 (1 < 𝐾 < 𝑁).
Pomiędzy wszystkie elementy wybranego fragmentu możemy wstawiać operatory dodawania albo
mnożenia, tak aby powstało wyrażenie arytmetyczne. W powstałym wyrażeniu nie mogą wystąpić
dwa jednakowe operatory obok siebie. Interesuje nas znalezienie takiego fragmentu ciągu, który
pozwala zbudować wyrażenie o wartości będącej liczbą pierwszą, taką że stosunek tej liczby pierwszej
do długości znalezionego fragmentu jest największy. Proszę napisać funkcję find_max(T), która dla
ciągu zawartego w tablicy T, wyznaczy wartość maksymalnego ilorazu jaki można znaleźć. Jeżeli taki
podciąg nie istnieje funkcja powinna zwrócić wartość zero.
Na przykład dla ciągu: 7, 8, 6, 4, 7, 3 funkcja powinna zwrócić wartość 16.6.
Możliwe podciągi dające liczby pierwsze to:
7 + 8 ⋅ 6 + 4 = 59, 59/4 = 14.75
7 + 8 ⋅ 6 + 4 ∗ 7 = 83, 83/5 = 16.6
6 ⋅ 4 + 7 = 31, 31/3 = 10.(3)
4 + 7 = 11, 11/2 = 5.5
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


def find_max(T):
    final_result = 0
    result = 0
    N = len(T)

    for k in range(2, N):
        for i in range(N - k + 1):
            stos_dodawanie = []  # dodawanie jest pierwsze
            stos_mnozenie = []  # mnozenie jest pierwsze
            flaga = True  # True jest wtedy kiedy wykonujemy mnozenie, na stosie gdzie mnozenie jest pierwsza operacja
            for indeks in range(i, i + k):
                stos_mnozenie.append(T[indeks])
                stos_dodawanie.append(T[indeks])

                if indeks == i:
                    continue

                if flaga:
                    flaga = False
                    a = stos_mnozenie.pop()
                    b = stos_mnozenie.pop()
                    stos_mnozenie.append(a * b)
                else:
                    flaga = True
                    a = stos_dodawanie.pop()
                    b = stos_dodawanie.pop()
                    stos_dodawanie.append(a * b)

            suma_dodawania = sum(stos_dodawanie)
            suma_mnozenie = sum(stos_mnozenie)

            if isPrime(suma_dodawania):
                result = suma_dodawania / k
                if final_result < result:
                    final_result = result

            if isPrime(suma_mnozenie):
                result = suma_mnozenie / k
                if final_result < result:
                    final_result = result

    return final_result

print(find_max(T))