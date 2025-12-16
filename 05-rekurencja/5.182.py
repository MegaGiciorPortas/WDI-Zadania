"""
Zadanie 182. def hanoi(n,a,b,c):
if n>0:
hanoi(n-1,a,c,b)
print(a,’->’,c)
hanoi(n-1,b,a,c)
Dana jest funkcja rozwiązująca problem wież Hanoi:
- Usunąć rekurencję zastępując ją stosem,
- Zaimplementować algorytm bez użycia stosu ani rekurencji (wikipedia
"""


def hanoi_stack(n, source, aux, target):
    # Stos przechowuje krotki: (ile_dysków, skąd, przez_co, dokąd)
    stack = [(n, source, aux, target)]

    while stack:
        n, a, b, c = stack.pop()

        if n == 1:
            # Base case: fizyczne przeniesienie krążka
            print(f"{a} -> {c}")
        else:
            # Wrzucamy na stos w odwrotnej kolejności wykonywania!

            # Krok 3: Przenieś n-1 z pomocniczego (b) na docelowy (c)
            stack.append((n - 1, b, a, c))

            # Krok 2: Przenieś ten jeden największy z (a) na (c)
            # Uwaga: wrzucam to jako n=1, żeby w następnym obiegu wpadło w if n==1
            stack.append((1, a, b, c))

            # Krok 1: Przenieś n-1 ze źródła (a) na pomocniczy (b)
            stack.append((n - 1, a, c, b))


# Test
print("--- Wersja ze stosem ---")
hanoi_stack(3, 'A', 'B', 'C')


def hanoi_iterative(n, source, aux, target):
    # Obliczamy całkowitą liczbę ruchów: 2^n - 1
    total_moves = (2 ** n) - 1

    # Tworzymy słupki jako listy, żeby wiedzieć, co leży na szczycie
    # Na słupku źródłowym układamy dyski: [3, 2, 1] (1 jest na górze)
    pegs = {
        source: list(range(n, 0, -1)),
        aux: [],
        target: []
    }

    # Dla parzystej liczby krążków zamieniamy rolami słupek pomocniczy i docelowy
    # (Zasada algorytmu iteracyjnego)
    if n % 2 == 0:
        aux, target = target, aux

    # Lista nazw słupków w kolejności cyklicznej: S -> T -> A -> S...
    # Kolejność w tablicy: [0: source, 1: target, 2: aux]
    cycle = [source, target, aux]

    # Funkcja pomocnicza wykonująca legalny ruch między dwoma słupkami
    def move_disk(peg1_name, peg2_name):
        peg1 = pegs[peg1_name]
        peg2 = pegs[peg2_name]

        # Jeśli słupek 1 jest pusty, musimy przenieść z 2 na 1
        if not peg1:
            disk = peg2.pop()
            peg1.append(disk)
            print(f"{peg2_name} -> {peg1_name}")
        # Jeśli słupek 2 jest pusty, przenosimy z 1 na 2
        elif not peg2:
            disk = peg1.pop()
            peg2.append(disk)
            print(f"{peg1_name} -> {peg2_name}")
        # Jeśli na obu coś jest, porównujemy wielkość
        elif peg1[-1] < peg2[-1]:
            disk = peg1.pop()
            peg2.append(disk)
            print(f"{peg1_name} -> {peg2_name}")
        else:
            disk = peg2.pop()
            peg1.append(disk)
            print(f"{peg2_name} -> {peg1_name}")

    # Główna pętla
    for i in range(1, total_moves + 1):
        if i % 3 == 1:
            move_disk(source, target)
        elif i % 3 == 2:
            move_disk(source, aux)
        elif i % 3 == 0:
            move_disk(aux, target)


# Test
print("\n--- Wersja iteracyjna ---")
# Uwaga: Dla wersji iteracyjnej zamiana ról przy parzystych n dzieje się wewnątrz funkcji,
# więc wywołujemy normalnie: A -> C używając B
hanoi_iterative(3, 'A', 'B', 'C')
