samogloski = "AEIOUY"


def addition(a, b):
    global samogloski

    if a in samogloski and b in samogloski:
        return min(a, b)
    elif a in samogloski:
        return a
    elif b in samogloski:
        return b
    else:
        return max(a, b)


def multiplication(a, b):
    global samogloski

    if a in samogloski and b in samogloski:
        return max(a, b)
    elif a in samogloski:
        return b
    elif b in samogloski:
        return a
    else:
        return min(a, b)


def executing_brackets(values, operators):
    while operators[-1] != "(":
        operation = operators.pop()
        val_b = values.pop()
        val_a = values.pop()
        if operation == "+":
            values.append(addition(val_a, val_b))
        else:
            values.append(multiplication(val_a, val_b))

    operators.pop()


def main_function(napis):
    napis = "(" + napis + ")"
    values = []
    operators = []
    for i in range(len(napis)):
        if 65 <= ord(napis[i]) <= 90:
            values.append(napis[i])
        else:
            if napis[i] == ")":
                executing_brackets(values, operators)
            else:
                if napis[i] == "(":
                    operators.append(napis[i])
                else:
                    if operators and operators[-1] == "*":
                        val_b = values.pop()
                        val_a = values.pop()
                        operators.pop()
                        values.append(multiplication(val_a, val_b))
                        operators.append(napis[i])
                    else:
                        operators.append(napis[i])

    return values[0]


napis = input("").strip()
print(main_function(napis))
