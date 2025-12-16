"""
Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy jej
cyfry stanowia ciag rosnacy
"""


def czy_rosnacy(n):
    a1 = n % 10
    n //= 10
    while n > 0:
        if n % 10 >= a1:
            return False
        a1 = n % 10
        n //= 10
    return True


n = int(input("n: "))
print(czy_rosnacy(n))