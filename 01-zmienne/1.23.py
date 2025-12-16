"""
Prosze napisac program wyznaczajacy wartosc liczby e korzystajac z zaleznosci:
e = 1/0! + 1/1! + 1/2! + ...
"""

e = 1
w = 1
liczba = 2
while w > 0:
    e += w
    w /= liczba
    liczba += 1

print(e)