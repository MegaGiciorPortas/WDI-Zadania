"""
Dana jest tablica T zawierająca liczby naturalne. W tablicy na kolejnych pozycjach ukryto
pewien ciąg liczb o długości co najmniej 3 elementów. Aby ułatwić odnalezienie tego ciągu, zaraz za nim
umieszczono ten sam ciąg, ale każdy z jego elementów pomnożono przez pewną liczbę. Proszę napisać funkcję
sequence(T) która odnajdzie ukryty ciąg. Funkcja powinna zwrócić indeksy pierwszego i ostatniego elementu
ukrytego ciągu. Na przykład dla ciągu: 2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2 funkcja zwróci 4,7
"""


def czy_ciag_poprawny(ciag):
    srodek = len(ciag) // 2
    a1 = ciag[0]
    a2 = ciag[srodek]
    # a2/a1 == b2/b1 --> a1*b2 == a2*b1
    for i in range(1, srodek):
        if a1 * ciag[i+srodek] != a2 * ciag[i]:
            return False
    return True


def main_funciton(T):
    N = len(T)

    for dlugosc in range(6, N + 1, 2):
        for i in range(N - dlugosc + 1):
            ciag = T[i:i + dlugosc]
            if czy_ciag_poprawny(ciag):
                return i, i + (dlugosc // 2) - 1

    return None


T = [2, 5, 7, 3, 2, 3, 5, 7, 6, 9, 15, 21, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 1, 3, 2]
print(main_funciton(T))
