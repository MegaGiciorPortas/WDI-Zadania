"""
Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
ta zakończona jest unikalną cyfrą.
"""


def funkcja(n):
    last = n % 10
    n //= 10

    while n > 0:
        if n % 10 == last:
            return False
        n //= 10
    return True


n = int(input("n: "))
print(funkcja(n))
