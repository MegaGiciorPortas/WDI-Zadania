"""
Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakoń-
czonych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.
"""

tablica = [0 for _ in range(10)]
licznik = 0

while True:
    a = int(input("a: "))

    if a == 0:
        break

    if tablica[9] != 0:
        if tablica[9] < a:
            tablica[9] = a
            tablica.sort(reverse = True)

    else:
        tablica[licznik] = a
        licznik += 1
        if licznik == 10:
            tablica.sort(reverse = True)

print(tablica[9])