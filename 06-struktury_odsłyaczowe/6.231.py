"""
Lista odsyłaczowa zbudowana jest z obiektów zawierających dwa pola: val przechowujące
liczbę naturalną oraz pole next przechowujące wskaźnik do kolejnego elementu. Dane była niepusta lista
odsyłaczowa, która zawierała rosnący ciąg wartości val. Przez pomyłkę spójny fragment tej listy liczący 6
elementów został przeniesiony w inne miejsce w liście. Proszę napisać funkcję fix(p), która naprawia taką
listę, tak aby przywrócić rosnący porządek elementów. Do funkcji przekazujemy wskaźnik na listę, funkcja
powinna zwrócić dwa wskaźniki na naprawioną listę.
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def fix(first):
    cur = first
    start = None
    meta = None

    while cur is not None and cur.next is not None:
        if cur.val > cur.next.val:
            A = cur
            B = cur.next
            # [A][B][0][1][2][3][4]
            flaga = False
            for i in range(5):
                # ten warunek powinien zalatwic sprawe
                if i < 4 and cur.next is None:
                    flaga = True
                    break
                cur = cur.next
                if A.val < cur.val:  # zachodzi sytaucja B
                    flaga = True
                    break
            if cur.next is not None and A.val > cur.next.val:
                flaga = True
            if flaga:
                if first.val > B.val:
                    start = first
                    meta = A
                    first = B
                else:
                    p = None
                    q = first

                    while q is not None:
                        if q.val > B.val:
                            p.next = B
                            start = q
                            meta = A
                            break
                        p = q
                        q = q.next.
            else:
                start = B
                meta = cur
                A.next = cur.next
            break

            cur = cur.next

    if start == meta and start == None:
        return first

    if first.val > start.val:
        meta.next = first
        return start
    else:
        p = None
        q = first

        while q is not None:
            if q.val > start.val:
                p.next = start
                meta.next = q
                break
            p = q
            q = q.next

        return first
