"""
Pierwiastek całkowitoliczbowy z liczby naturalnej to część całkowita z pierwiastka z tej liczby.
Proszę napisać program obliczający taki pierwiastek korzystając z zależności 1 + 3 + 5 +...= n^2

"""
s = int(input("s: "))

i = 1
suma = 0
n = 0

while suma <= s:
    print(suma, i, n)
    suma += i
    i += 2
    n += 1

print(n - 1)
