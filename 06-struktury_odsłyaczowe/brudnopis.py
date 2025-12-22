# def primes():
#     lp = [2]
#     p = 2
#     yield p
#     while True:
#         p += 1
#         for d in lp:
#             if p % d == 0:
#                 break
#         else:
#             yield p
#             lp.append(p)
#
#
# def twins():
#
#     g = primes()
#     w1 = next(g)
#     while True:
#         w2 = next(g)
#         if w2 - w1 == 2:
#             yield w1, w2
#         w1 = w2
#
#
# generator = twins()
# while True:
#     print(next(generator))

def gen(n):
    if n == 0:
        yield ""
    else:
        g = gen(n-1)
        while True:
            try:
                c = next(g)
                yield c + "0"
                yield c + "1"
            except StopIteration:
                break

for x in gen(4):
    print(x)