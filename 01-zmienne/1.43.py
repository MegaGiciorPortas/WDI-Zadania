"""
Proszę napisać funkcję, która zwraca wartość True gdy dwie liczby są zbudowane z tych
samych cyfr (na przykład: 123 i 231, 5749 i 4597) i wartość False w przeciwnym przypadku.
"""
n1 = input("n1: ")
n2 = input("n2: ")
sort_n1 = "".join(sorted(n1))
sort_n2 = "".join(sorted(n2))

if sort_n1 == sort_n2:
    print(True)
else:
    print(False)
