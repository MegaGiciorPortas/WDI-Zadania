class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def delete(first):
    if not first or not first.next:
        return first

    m1, m2 = float('inf'), float('inf')
    M1, M2 = float('-inf'), float('-inf')
    suma_wszystkich = 0
    n = 0

    curr = first
    while curr:
        v = curr.val
        suma_wszystkich += v
        n += 1

        # Logika szukania dwóch najmniejszych
        if v < m1:
            m1, m2 = v, m1
        elif v < m2:
            m2 = v

        # Logika szukania dwóch największych
        if v > M1:
            M1, M2 = v, M1
        elif v > M2:
            M2 = v
        curr = curr.next

    if n < 3:  # Zbyt mało elementów, by mówić o ciągu arytmetycznym i intruzie
        return first

    hipotezy = [
        (m1, M1, None),  # Intruz jest w środku, krańce są OK
        (m2, M1, m1),  # m1 jest intruzem, ciąg zaczyna się od m2
        (m1, M2, M1)  # M1 jest intruzem, ciąg kończy się na M2
    ]

    wrong_value = None

    for start, end, candidate in hipotezy:
        if n > 2:
            r = (end - start) // (n - 2)
        else:
            r = 0  # Przypadek brzegowy

        teoretyczna_suma = (start + end) * (n - 1) // 2

        poszlaka = suma_wszystkich - teoretyczna_suma

        if candidate is not None:
            if poszlaka == candidate:
                wrong_value = candidate
                break
        else:
            wrong_value = poszlaka
            break

    if first.val == wrong_value:
        return first.next

    prev = first
    curr = first.next
    while curr:
        if curr.val == wrong_value:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next

    return first
