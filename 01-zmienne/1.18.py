"""
Proszę napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina.
"""
import math

x = int(input("x: "))
precision = int(input("precision: "))
x = ((x % 360) / 180) * math.pi

cos_value = 0
for n in range(precision):
    cos_value += ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)

print(round(cos_value, 4))
