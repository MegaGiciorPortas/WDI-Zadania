"""
Nieskończony iloczyn sqrt(0.5) * sqrt(0.5 + 0.5 *sqrt(0.5)) * sqrt(0.5 + 0.5 * sqrt(0.5 + 0.5 * sqrt(0.5))) *... ma
wartość 2/π. Proszę napisać program korzystający z tej zależności i wyznaczający wartość π.
"""
import math

a = math.sqrt(0.5)
p = a
for i in range(int(10e4)):
    a = math.sqrt(0.5 + 0.5 * a)
    p *= a

pi = 2 / p
print(pi)
