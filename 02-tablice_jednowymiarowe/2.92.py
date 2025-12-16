"""
Korzystając z funkcji z poprzedniego zadania oraz wiedząc, że 1 stycznia 1900 roku był
poniedziałek, proszę napisać program obliczający jaki dzień tygodnia przypada na określoną datę
"""


def czy_przestepny(n):
    return (n % 4 == 0 and n % 100 != 0) or n % 400 == 0


def ile_dni_do_epoki(data):
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


def jaki_dzien_tygodnia(liczba):
    if liczba % 7 == 0:
        return "niedziela"
    elif liczba % 7 == 1:
        return "poniedzialek"
    elif liczba % 7 == 2:
        return "wtorek"
    elif liczba % 7 == 3:
        return "sroda"
    elif liczba % 7 == 4:
        return "czwartek"
    elif liczba % 7 == 5:
        return "piatek"
    else:
        return "sobota"


def jaki_dzien_tygodania(data):
    data = data.split(".")
    # 01.01.1900 - poniedzialek
    ilosc_dni = ile_dni_do_epoki(data)

    dzien_tygodnia = jaki_dzien_tygodnia(ilosc_dni)

    return dzien_tygodnia


data1 = "19.05.1964"
data2 = "21.06.1970"
print(jaki_dzien_tygodania(data1))
print(jaki_dzien_tygodania(data2))
