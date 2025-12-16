"""
Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe
odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce
"""


def recurencion(T, wynik, indeks = 0, suma = 0):
    if indeks == len(T):
        if suma == wynik:
            return True
        return False

    if suma > wynik:
        return False
    
    return recurencion(T, wynik, indeks + 1, suma + T[indeks]) or recurencion(T, wynik, indeks + 1, suma)


masa = int(input("masa: "))
T = [1, 2, 5, 10, 25, 50]
print(recurencion(T, masa))
