"""
Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej sumie

"""
import sys

n = int(input("n: "))
sum = 0
a = 1
b = 1
while sum < n:
    sum += a
    a, b = b, a + b

    if sum == n:
        print("Tak")
        sys.exit(0)

a = 1
b = 1
while sum > n:
    sum -= a
    a, b = b, a + b

    if sum == n:
        print("Tak")
        sys.exit(0)

print("Nie")
