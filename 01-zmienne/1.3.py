"""
Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.
"""

a = 1
b = 1

while a < 1e6:
    print(a)
    c = a + b
    a = b
    b = c
