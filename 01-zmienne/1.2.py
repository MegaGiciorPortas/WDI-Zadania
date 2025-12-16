"""
Proszę napisać program odnajdujący cyfry a,b,c w działaniu: abc+ abc+ abc= bbb.

3*(a*100 + b*10 + c) = 111b
300a + 30b + 3c = 111b
300a + 3c = 81b
"""

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if 300 * a + 3 * c == 81 * b:
                print(a, b, c)
