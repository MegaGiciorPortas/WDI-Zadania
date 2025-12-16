from random import randint


# Twoja funkcja sprawdzająca palindrom jest niepotrzebna,
# ponieważ sprawdzamy to w pętli głównej.

def funkcja_main(T):
    N = len(T)
    najdluzszy_palindrom = 0

    # Iterujemy przez KAŻDY możliwy ŚRODEK palindromu
    # W C++: for (int i = 0; i < N; i++)
    for i in range(N):

        # --- 1. Sprawdź palindromy NIEPARZYSTEJ długości (centrum w 'i') ---
        # Np. [3, (5), 3]

        # Sprawdzamy, czy sam środek jest parzysty.
        # Jeśli tak, nie może być częścią nieparzystego palindromu.
        if T[i] % 2 == 0:
            continue  # Przejdź do następnego 'i'

        # Jeśli środek jest OK (nieparzysty), ustawiamy długość na 1
        # i rozszerzamy wskaźniki
        l, r = i - 1, i + 1  # Lewy i prawy wskaźnik
        aktualna_dlugosc = 1
        najdluzszy_palindrom = max(najdluzszy_palindrom, aktualna_dlugosc)

        while l >= 0 and r < N:
            # Sprawdź, czy oba końce są nieparzyste I czy są równe
            if T[l] % 2 == 1 and T[r] % 2 == 1 and T[l] == T[r]:
                # Palindrom trwa, rozszerzamy go
                aktualna_dlugosc = r - l + 1
                najdluzszy_palindrom = max(najdluzszy_palindrom, aktualna_dlugosc)
                l -= 1
                r += 1
            else:
                # Palindrom (lub ciąg nieparzysty) przerwany
                break

        # --- 2. Sprawdź palindromy PARZYSTEJ długości (centrum między 'i' a 'i+1') ---
        # Np. [3, (5, 5), 3]

        # Sprawdzamy, czy centrum (i, i+1) jest OK
        if i + 1 < N and T[i] % 2 == 1 and T[i + 1] % 2 == 1 and T[i] == T[i + 1]:
            l, r = i - 1, i + 2
            aktualna_dlugosc = 2
            najdluzszy_palindrom = max(najdluzszy_palindrom, aktualna_dlugosc)

            while l >= 0 and r < N:
                if T[l] % 2 == 1 and T[r] % 2 == 1 and T[l] == T[r]:
                    aktualna_dlugosc = r - l + 1
                    najdluzszy_palindrom = max(najdluzszy_palindrom, aktualna_dlugosc)
                    l -= 1
                    r += 1
                else:
                    break

    return najdluzszy_palindrom


# --- Uruchomienie ---
N = int(input("N: "))
T = [randint(1, 1000) for _ in range(N)]
print(T)

# Test z Twojego przykładu:
# T = [1, 2, 3, 5, 3, 8, 1, 3, 2]
# (poprawnie zwróci 3 dla [3, 5, 3])
# T = [1, 9, 3, 5, 3, 9, 2]
# (poprawnie zwróci 3 dla [3, 5, 3])

print(funkcja_main(T))