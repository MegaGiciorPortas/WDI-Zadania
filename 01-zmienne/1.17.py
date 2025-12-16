"""
Prosze napisac program wyznaczajcy najmniejsza wspolna wielokrotnosc 3 pddanych liczb
"""

def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def nww(a, b):
    return abs(a * b) / nwd(a, b)


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

krok1 = nww(a, b)
wynik = nww(krok1, c)
print(wynik)
