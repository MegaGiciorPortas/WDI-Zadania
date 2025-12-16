"""
Proszę napisać funkcję, która oblicza ile dni dzieli dwie daty. Na przykład daty 19.05.1964
i 21.06.1970 dzieli 2224 dni. Do funkcji należy przekazać obie daty, funkcja powinna zwrócić liczbę dni
pomiędzy tymi datami. Daty mogą pochodzić z lat 1900-2100
"""


def czy_przestepny(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        return True
    return False


def ile_dni_do_epoki(data):
    # 01.01.1900
    suma_dni = 0
    for rok in range(1900, int(data[2])):
        if czy_przestepny(rok):
            suma_dni += 366
        else:
            suma_dni += 365

    ilosc_dni_w_miesiacach = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for j in range(1, int(data[1])):
        suma_dni += ilosc_dni_w_miesiacach[j]

    if czy_przestepny(int(data[2])) and int(data[1]) > 2:
        suma_dni += 1
    suma_dni += int(data[0])

    return suma_dni


def ile_dni_dzieli_daty(data1, data2):
    data1 = data1.split(".")
    data2 = data2.split(".")
    dni_do_epoki_data1 = ile_dni_do_epoki(data1)
    dni_do_epoki_data2 = ile_dni_do_epoki(data2)
    print(dni_do_epoki_data1,dni_do_epoki_data2)

    return dni_do_epoki_data2 - dni_do_epoki_data1


data1 = "19.05.1964"
data2 = "21.06.1970"
print(ile_dni_dzieli_daty(data1, data2))
