"""
Dany jest ciąg N liczb naturalnych, z którego wybieramy spójny fragment o długości K
(1 <K <N). Pomiędzy wszystkie elementy wybranego fragmentu możemy wstawiać operatory dodawania
albo mnożenia, tak aby powstało wyrażenie arytmetyczne. W powstałym wyrażeniu nie mogą wystąpić dwa
jednakowe operatory obok siebie. Interesuje nas znalezienie takiego fragmentu ciągu, który pozwala zbu-
dować wyrażenie o wartości będącej liczbą pierwszą. Proszę napisać funkcję find max(T), która dla ciągu
zawartego w tablicy T, wyznaczy wartość największej liczby pierwszej, jaką można znaleźć. Jeżeli taki pod-
ciąg nie istnieje, funkcja powinna zwrócić wartość zero.
Na przykład dla ciągu: 7,8,6,4,7,3 funkcja powinna zwrócić wartość 83
Możliwe podciągi dające liczby pierwsze to:
7 + 8 ∗6 + 4 = 59
7 + 8 ∗6 + 4 ∗7 = 83
6 ∗4 + 7 = 31
4 + 7 = 11
"""
