"""
Problem wież w Hanoi (treść oczywista)
"""


def hanoi(n, a, b, c):
    if n == 0: return
    print(n,a,b,c)
    hanoi(n - 1, a, c, b)
    print(a, "-->", c)
    hanoi(n - 1, b, a, c)


n = int(input("n: "))
hanoi(n, "A", "B", "C")
