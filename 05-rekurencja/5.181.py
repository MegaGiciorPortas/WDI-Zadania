"""
wzorem rekurencyjnym:
def f(a,b):
if a==0: return b+1
if b==0: return f(a-1,1)
return f (a-1,f(a,b-1))
Dana jest funkcja Ackermana, określona na zbiorze liczb całkowitych nieujemnych, dana
Proszę napisać funkcję w wersji iteracyjnej
"""


def ackermann_iterative(a, b):
    # 1. Tworzymy stos i wrzucamy na niego pierwszą wartość 'a'
    stack = [a]

    # 2. Pętla działa tak długo, jak mamy coś na stosie
    while stack:
        # 3. Zdejmujemy 'a' z wierzchu stosu
        a = stack.pop()

        # --- Tłumaczenie warunków z treści zadania ---

        # Warunek 1: if a == 0: return b + 1
        if a == 0:
            b = b + 1

        # Warunek 2: if b == 0: return f(a-1, 1)
        elif b == 0:
            stack.append(a - 1)  # Zaplanuj a-1
            b = 1  # Ustaw b na 1

        # Warunek 3: return f(a-1, f(a, b-1))
        else:
            # Tu jest "magia" kolejności:
            # Najpierw wrzucamy to, co ma być policzone PÓŹNIEJ (zewnętrzne a-1)
            stack.append(a - 1)

            # Potem wrzucamy to, co ma być policzone TERAZ (wewnętrzne a)
            stack.append(a)

            # Zmniejszamy b (argument wewnętrzny)
            b = b - 1

    # 4. Gdy stos jest pusty, b zawiera wynik
    return b


# --- Testy ---
print(f"Ackermann(1, 1) = {ackermann_iterative(1, 1)}")  # Powinno być 3
print(f"Ackermann(2, 2) = {ackermann_iterative(2, 2)}")  # Powinno być 7
print(f"Ackermann(3, 2) = {ackermann_iterative(3, 2)}")  # Powinno być 29
