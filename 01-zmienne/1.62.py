"""
Dwie liczby naturalne A,B można ”skleić” ze sobą jeżeli 2 lub 3 ostatnie cyfry liczby A
pookrywają się z odpowiednio z pierwszymi 2 lub 3 cyframi liczby B. Na przykład: 2571 i 710, 12345678
i 678999. Siła z jaką sklejone są liczby to liczba złożona z dopasowanych cyfr, dla powyższych przykładów
to odpowiednio: 71 i 678. Dany jest cykl złożony z N 8 cyfrowych liczb, zawarty w tablicy T. Proszę
napisać funkcję, która w takim cyklu znajdzie fragment o największej, sumarycznej sile sklejenia. Funk-
cja powinna zwrócić siłę sklejenia znalezionego cyklu. W przypadku gdy żadnych dwóch kolejnych liczb nie
uda się skleić, funkcja powinna zwrócić wartość 0. Jeżeli uda się skleić cały cykl funkcja powinna zwrócić−1.
Dla tablicy: T = [79000023,23111134,55555555,66666104,10467700,88888879]
Funkcja powinna zwrócić wartość 104 (elementy o indeksach 3,4), inny ciąg złożony z elementów o indeksach
5,0,1 ma siłę sklejenia 79+23=102
"""


def sprawdzenie_skejenia(a, b):
    if a % 1000 == b // int(1e5):
        return a % 1000
    if a % 100 == b // int(1e6):
        return a % 100
    return 0


def sila_sklejenia(tablica, indeks):
    if tablica[indeks] == 0:
        return 0
    suma = tablica[indeks]
    nowy_indeks = indeks
    dlugosc = len(tablica)
    while True:
        if nowy_indeks == indeks:
            if tablica[(indeks + 1) % dlugosc] != 0:
                suma += tablica[(indeks + 1) % dlugosc]
                nowy_indeks += 2
            else:
                return suma
        else:
            if tablica[nowy_indeks % dlugosc] != 0:
                suma += tablica[nowy_indeks % dlugosc]
                nowy_indeks += 1
            else:
                return suma


N = int(input("N: "))
T = [0 for _ in range(N)]
for i in range(N):
    T[i] = int(input(f"Podaj liczbe nr.{i + 1}: "))

tablica_sklejen = [0 for _ in range(N)]
for i in range(N):
    if i + 1 == N:
        tablica_sklejen[i] = sprawdzenie_skejenia(T[i], T[0])
    else:
        tablica_sklejen[i] = sprawdzenie_skejenia(T[i], T[i + 1])

moce_cykli = [sila_sklejenia(tablica_sklejen, indeks) for indeks in range(N)]
    if max(moce_cykli) == sum(tablica_sklejen) and not 0 in tablica_sklejen:
        print(-1)
    else:
        print(max(moce_cykli))
