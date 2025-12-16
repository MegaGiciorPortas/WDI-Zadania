"""
Ciąg liczb naturalnych jest zawarty w tablicy T. Proszę napisać funkcję sequence(T) któ-
ra sprawdza, czy jest możliwe pocięcie ciągu na kawałki w taki sposób, aby sumy elementów w kolejnych
kawałkach stanowiły rosnący ciąg arytmetyczny. Funkcja powinna zwrócić wartość pierwszego wyrazu tego
ciągu oraz jego różnicę. Jeżeli utworzenie tego ciągu jest niemożliwe, funkcja powinna zwrócić wartość None.

Przykład: Dla ciągu: 2,3,5,3,3,7,3,7,23,11,13,5 funkcja powinna zwrócić wartości 5,6 powstały ciąg to 5,11,17,23,29
"""


def recurension(T, indeks, diff, current, wanted):
    if indeks >= len(T):
        return current == 0 or current == wanted

    if current > wanted:
        return False

    if current == wanted:
        return recurension(T, indeks + 1, diff, T[indeks], wanted + diff)

    return recurension(T, indeks + 1, diff, current + T[indeks], wanted)


def sequence(T):
    for i in range(1, len(T)):
        a1 = sum(T[:i])
        for j in range(1, len(T) - i + 1):
            a2 = sum(T[i:i + j])
            difference = a2 - a1

            if difference <= 0:
                return None

            indeks = i + j

            if recurension(T, indeks, difference, 0, a1 + 2 * difference):
                return a1, difference
    return None


T = [2, 3, 5, 3, 3, 7, 3, 7, 23, 11, 13, 5]
print(f"{T}: {sequence(T)}")
T1 = [1, 2, 3, 4, 5]
print(f"{T1}: {sequence(T1)}")
T2 = [1, 2, 6, 9]
print(f"{T2}: {sequence(T2)}")
T3 = [1, 10, 2, 3]
print(f"{T3}: {sequence(T3)}")
T4 = [10, 20]
print(f"{T4}: {sequence(T4)}")
T5 = [4, 6, 2, 8, 4, 16]
print(f"{T5}: {sequence(T5)}")
