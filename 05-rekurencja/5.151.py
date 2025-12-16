"""
Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników
niż 2,3,5. Jedynka też jest taką liczbą. Proszę napisać funkcję rekurencyjną, wypisującą liczby znajdujące
się w przedziale od 1 do N włącznie
"""


def generate(N, actual_number = 1, last_multiplicator = 2):
    if actual_number > N:
        return
    print(actual_number)

    if last_multiplicator <= 2:
        generate(N, actual_number * 2, 2)
    if last_multiplicator <= 3:
        generate(N, actual_number * 3, 3)
    if last_multiplicator <= 5:
        generate(N, actual_number * 5, 5)


N = int(input("N: "))
generate(N)