"""
Proszę napisać program obliczający i wypisujący wartość N! dla N z zakresu od 1 do 1000
"""
def silnia(n):
    tablica = [1]
    for i in range(2, n + 1):
        carry = 0
        for j in range(len(tablica)):
            temp = tablica[j] * i + carry
            tablica[j] = temp % 10
            carry = temp // 10
        while carry > 0:
            tablica.append(carry % 10)
            carry = carry // 10

    tablica.reverse()
    print("".join(map(str,tablica)))


n = int(input("n: "))
silnia(n)