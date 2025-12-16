"""
Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w
sensie liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów
tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego
podzbioru. Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10, są to elementy o indeksach
2,3,i 5.
"""
minSum = float('inf')
minEl = float('inf')


def recurension(T, indeks = 0, sumaLiczb = 0, sumaIndeksow = 0, liczbaElementow = 0):
    global minEl, minSum
    if indeks == len(T):
        if sumaIndeksow == sumaLiczb and liczbaElementow != 0:
            if liczbaElementow < minEl:
                minEl = liczbaElementow
                minSum = sumaLiczb
        return
    recurension(T, indeks + 1, sumaLiczb, sumaIndeksow, liczbaElementow)
    recurension(T, indeks + 1, sumaLiczb + T[indeks], sumaIndeksow + indeks, liczbaElementow + 1)


def main(T):
    global minSum, minEl
    minEl = float('inf')
    minSum = float('inf')
    recurension(T)
    return minSum


def cppStyle(T, results, indeks = 0, sumaLiczb = 0, sumaIndeksow = 0, liczbaElementow = 0):
    if indeks == len(T):
        if sumaIndeksow == sumaLiczb:
            if liczbaElementow > 0 and liczbaElementow < results[0]:
                results[0] = liczbaElementow
                results[1] = sumaLiczb
        return
    if liczbaElementow > results[0] and results[0] != float('inf'):
        return
    cppStyle(T, results, indeks + 1, sumaLiczb, sumaIndeksow, liczbaElementow)
    cppStyle(T, results, indeks + 1, sumaLiczb + T[indeks], sumaIndeksow + indeks, liczbaElementow + 1)


def cppMain(T):
    #       liczba_elementow, suma
    lista = [float('inf'), 0]
    cppStyle(T, lista)
    if lista[0] != float('inf'):
        return lista[1]
    return None


T = [1, 7, 3, 5, 11, 2]
print(main(T))
print(cppMain(T))
