"""
Proszę napisać program, który oblicza pole figury pod wykresem funkcji y= 1/xw przedziale
od 1 do k, metoda prostokatow
"""

n = int(input("Podaj ilosc prostokatow: "))
k = int(input("k: "))

dx = (k - 1) / n
suma = 0.0

for i in range(n):
    x = 1 + i * dx
    sr = (x + x + dx) / 2
    y = 1 / sr
    suma += dx * y

print(suma)
