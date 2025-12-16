"""
Proszę zmodyfikować wzór Newtona aby program z poprzedniego zadania obliczał pierwiastek stopnia 3.
"""
s = int(input("n: "))
eps = 1e-6
a = 1
diff = -a

while abs(diff) > eps:
    diff = -a
    a = (1 / 3) * (s / (a * a) + 2 * a)
    diff += a

print(a)
