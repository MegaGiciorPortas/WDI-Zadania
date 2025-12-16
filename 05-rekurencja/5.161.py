"""
Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą
liczbę samogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład′′ula′′→
117,108,97 oraz ′′exe′′→101,120,101. Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe
zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna
wypisać znaleziony wyraz.
"""


def weight(s) -> tuple:
    vowels = "aeiouy"
    s1 = 0
    w1 = 0
    for char in s:
        s1 += ord(char)
        if char in vowels:  w1 += 1

    return s1, w1


def is_possible(w1, s2, res = "", position = 0) -> None:
    if position == len(s2):
        return w1 == weight(res)

    return is_possible(w1, s2, res + s2[position], position + 1) or is_possible(w1, s2, res, position + 1)


def word(s1, s2) -> bool:
    return is_possible(weight(s1), s2)
