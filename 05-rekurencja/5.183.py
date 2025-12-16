"""
Proszę napisać rekurencyjną funkcję obliczającą n-ty wyraz ciągu Fibonacciego ale tak aby
wewnątrz funkcji było tylko jedno odwołanie rekurencyjne
"""
def fib_single_call(n,a=0,b=1):
    if n == 0:
        return a
    return fib_single_call(n-1,b,a+b)


for n in range(2,15):
    print(f"{n}: {fib_single_call(n)}")
