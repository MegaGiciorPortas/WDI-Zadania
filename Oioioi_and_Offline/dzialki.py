def new_main_function(T):
    maxIncome = [0 for _ in range(len(T))]
    maxIncome[0] = T[0]
    maxIncome[1] = max(T[0], T[1])

    for i in range(2, len(T)):
        maxIncome[i] = max(maxIncome[i - 1], T[i] + maxIncome[i - 2])

    return max(maxIncome)


N = int(input(""))
T = []
for i in range(N):
    T.append(int(input("")))

print(new_main_function(T))
