"""
Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = n∗n+ n+ 1.
"""

x = int(input("Podaj liczbę naturalną: "))

found = False
n = 1

while True:
    a = n * n + n + 1
    print(n, a)
    if a > x:
        break
    if x % a == 0:
        found = True
        break
    n += 1

if found:
    print("TAK")
else:
    print("NIE")
