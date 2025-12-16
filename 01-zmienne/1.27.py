"""
Proszę napisać program wczytujący trzy liczby naturalne a,b,n i wypisujący rozwinięcie
dziesiętne ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)
"""

a = int(input("a: "))
b = int(input("b: "))
precision = int(input("precision: "))

print(a // b, end = "")
reszta = a % b
if precision > 0:
    print(".", end = "")
for i in range(precision):
    reszta *= 10
    print(reszta // b, end = "")
    reszta = reszta % b
