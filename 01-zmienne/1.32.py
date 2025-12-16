"""
Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3 * An−1 + 1, a pierwszy wyraz jest rowny 2
"""

n = int(input("n: "))

found = False
a = 2
while True:
    if a > n:
        break
    if n % a == 0:
        found = True
        break
    a = 3 * a + 1

if found:
    print("TAK")
else:
    print("NIE")
