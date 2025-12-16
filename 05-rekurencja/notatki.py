# iteracynje rozwiazanie dwumianu newtona
def newton_iteration(n, k):
    stos = [(n, k)]
    result = 0

    while stos:
        a, b = stos.pop()
        if b == 0 or b == a:
            result += 1
        else:
            stos.append((a - 1, b - 1))
            stos.append((a - 1, b))

    return result


n = int(input("n: "))
k = int(input("k: "))
print(newton_iteration(n, k))
