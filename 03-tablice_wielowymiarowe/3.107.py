"""
Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca war-
tość True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość
False w przeciwnym przypadku.
"""


def main_function(T):
    for wiersz in T:
        czy_jest_zero = False
        for element in wiersz:
            if element == 0:
                czy_jest_zero = True
        if not czy_jest_zero:
            return False

    for kolumna in range(len(T)):
        czy_jest_zero = False
        for wiersz in range(len(T)):
            if T[wiersz][kolumna] == 0:
                czy_jest_zero = True
            if not czy_jest_zero:
                return False
    return True


T = []
print(main_function(T))