"""
Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.
"""
n = int(input("n: "))

a = 1
b = 1
while a * b < n:
    a, b = b, a + b

if a * b == n:
    print(a, b)
else:
    print("Nie ma takich liczb! ")
