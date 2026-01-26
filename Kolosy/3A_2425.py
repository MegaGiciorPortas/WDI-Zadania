"""
Pewne państwo składa się z wysp leżących na kwadratowym oceanie. Położenie wysp opisuje kwadratowa
tablica T. Wartość T [w][k] > 0 oznacza powierzchnię wyspy o numerze równą wartości T [w][k]. Natomiast
wartość T [w][k] < 0 oznacza ocean o głębokości T [w][k]. Postanowiono połączyć wyspy mostami. Mosty
mogą przebiegać tylko w kierunku północ-południe albo wschód-zachód. Koszt mostu nad danym kwadratem
oceanu jest proporcjonalny do głębokości oceanu w tym kwadracie.
Proszę napisać funkcję bridge(T), która wyznaczy dwie dowolne wyspy o najmniejszym koszcie budowy
mostu łączącego te wyspy. Do funkcji należy przekazać tablicę opisującą położenie wysp, funkcja powinna
zwrócić numery wysp, pomiędzy którymi będzie budowany most. Można założyć, że istnieją wyspy, które
można połączyć mostem.
"""


def bridge(T):
    wyspa1 = 0
    wyspa2 = 0
    koszt = float('inf')

    wiersze = len(T)
    kolumny = len(T[0])

    for w in range(wiersze):
        last_island = 0
        current_cost = 0
        for k in range(kolumny):
            if T[w][k] > 0 and last_island == 0:
                last_island = T[w][k]
            elif T[w][k] > 0 and last_island != T[w][k]:
                if current_cost < koszt:
                    koszt = current_cost
                    wyspa1 = last_island
                    wyspa2 = T[w][k]
                last_island = T[w][k]
                current_cost = 0
            else:
                if T[w][k] < 0:
                    current_cost += abs(T[w][k])

    for k in range(kolumny):
        last_island = 0
        current_cost = 0
        for w in range(wiersze):
            if T[w][k] > 0 and last_island == 0:
                last_island = T[w][k]
            elif T[w][k] > 0 and last_island != T[w][k]:
                if current_cost < koszt:
                    koszt = current_cost
                    wyspa1 = last_island
                    wyspa2 = T[w][k]
                last_island = T[w][k]
                current_cost = 0
            else:
                current_cost += abs(T[w][k])

    return wyspa1, wyspa2


T = []
wyniki = bridge(T)
