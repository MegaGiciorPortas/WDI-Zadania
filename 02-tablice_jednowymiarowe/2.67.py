"""
Proszę napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e= 1/0! +
1/1! + 1/2! + 1/3! +... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).
"""

N = int(input("N: "))
e = [0 for _ in range(N + 1)]
w = [0 for _ in range(N + 1)]
e[0] = 1
w[0] = 1
m = 1

while sum(w) > 0:
    print(e,w,m)
    p = 0
    for i in range(N, -1, -1):
        e[i] = e[i] + w[i] + p
        p = e[i] // 10
        e[i] = e[i] % 10

    m += 1

    r = 0
    for i in range(N + 1):
        r = r * 10 + w[i]
        w[i] = r // m
        r = r % m

print(str(e[0]) + ".", end = "")
for i in range(1, len(e)):
    print(e[i], end = "")
