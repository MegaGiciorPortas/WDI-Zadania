"""
Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.
"""


def recurencion(T, masa, indeks = 0, lewaSzala = 0, prawaSzala = 0):
    if indeks == len(T):
        if masa == lewaSzala - prawaSzala:
            return True
        return False
    return (recurencion(T, masa, indeks + 1, lewaSzala + T[indeks], prawaSzala)
            or recurencion(T, masa, indeks + 1, lewaSzala, prawaSzala + T[indeks])
            or recurencion(T, masa, indeks + 1, lewaSzala, prawaSzala))


T = [3, 8, 20]
print(recurencion(T, 5), 5)
print(recurencion(T, 11), 11)
print(recurencion(T, 9), 9)
print(recurencion(T, 15), 15)
print(recurencion(T, 12), 12)
print(recurencion(T, 23), 23)
print(recurencion(T, 31), 31)
print(recurencion(T, 32), 32)
print(recurencion(T, 1), 1)
print(recurencion(T, 6), 6)
