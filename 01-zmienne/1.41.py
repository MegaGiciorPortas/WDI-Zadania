"""
roszę napisać funkcję, która sprawdza czy napis składający się z: liter a..z, operatorów
dodawania i mnożenie oraz nawiasów jest poprawnym wyrażeniem arytmetycznym.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()


n = input("napis: ")
stos = Stack()
flaga = True

# pusty napis -> niepoprawny
if not n:
    flaga = False

# sprawdź pierwszy znak: może być litera lub '('
if flaga:
    first = n[0]
    if not (first.isalpha() or first == "("):
        flaga = False

l = 0
while flaga and l < len(n):
    ch = n[l]
    prev = n[l - 1] if l > 0 else None

    if ch == "(":
        # '(' dozwolony po początku, po operatorze lub po '('
        if l == 0 or prev in ("(", "+", "*"):
            stos.push("(")
        else:
            flaga = False
            break

    elif ch == ")":
        # ')' dozwolone po az lub po ')'
        if prev is None or not (prev.isalpha() or prev == ")"):
            flaga = False
            break
        if stos.isEmpty():
            flaga = False
            break
        stos.pop()

    elif ch in ("+", "*"):
        # operator dozwolony tylko po az lub po ')'
        if not (l > 0 and (prev.isalpha() or prev == ")")):
            flaga = False
            break

    elif ch.isalpha():
        # az dozwolona na początku, po '(' lub po operatorze
        if l > 0 and not (prev in ("(", "+", "*")):
            flaga = False
            break

    else:
        flaga = False
        break

    l += 1

if flaga:
    if not stos.isEmpty():
        flaga = False
    if n[-1] in ("+", "*", "("):
        flaga = False

print("Napis poprawny" if flaga else "Napis niepoprawny")
