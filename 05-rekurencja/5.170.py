"""
Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A
cyfr 1 oraz B cyfr 0, gdzie A,B >0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca
ilość wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
10010(2),10100(2),11000(2)
"""
counter = 0


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def generate(a, b, result) -> None:
    global counter
    if a == 0 and b == 0:
        if not isPrime(result):
            counter += 1
        return

    if a != 0:
        generate(a - 1, b, 2 * result + 1)
    if b != 0:
        generate(a, b - 1, 2 * result)


def main_function(a, b) -> int:
    global counter
    if a == 1 and b == 0:
        return 0
    generate(a - 1, b, 1)
    return counter

print(main_function(2, 3))
