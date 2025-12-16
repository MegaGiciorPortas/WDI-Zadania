"""
Proszę napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb natural-
nych zakończonych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać te
elementy ciągu które są równe średniej arytmetycznej z 4 najbliższych sąsiadów. Na przykład dla ciągu:
2,3,2,7,1,2,4,8,5,2,2,5,7,9,3,1,0 powinny zostać wypisane liczby: 4,5. Można założyć, że w ciągu znajduje się
co najmniej 5 elementów.
"""

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
e = int(input("e: "))
wynik = ""
while e != 0:
    if c == (a + b + d + e) / 4:
        wynik += str(c) + ", "
    a = b
    b = c
    c = d
    d = e
    e = int(input("e: "))

print(wynik)
