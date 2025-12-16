"""
Dla ciągu z poprzedniego zadania proszę znaleźć najmniejszy wyraz początkowy N, dla
którego ciąg osiąga wartość 1 dokładnie po N krokach.
"""

for i in range(2, 10000):
    licznik = 0
    an = i
    while an != 1:
        an = (an % 2) * (3 * an + 1) + (1 - an % 2) * (an // 2)
        licznik += 1

    if licznik == i:
        print(f"Znaleziono: N = {i} (osiąga 1 po {licznik} krokach)")
        break