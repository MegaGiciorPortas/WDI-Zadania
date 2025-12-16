"""
Korzystajac z zaleznosc, że: (n po k) = (n-1 po k-1) + (n-1 po k)
napisz funkcje rekurencyjna
"""


def newton_sym(n, k) -> int:
    if n == k or k == 0:    return 1
    if k == 1:  return n
    if n - 1 == k:    return n

    return newton_sym(n - 1, k - 1) + newton_sym(n - 1, k)


print(newton_sym(5, 2))
