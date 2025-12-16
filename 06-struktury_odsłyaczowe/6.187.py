"""
wypisywanie elementów łańcucha
"""
'''
init
insert
remove
moc
member
empty
clear
suma zbiorow
czesc wspolna zbioru
zawieranie sie elementow zbioru
dopelnienie zbioru
'''


def czy_należy(p, x) -> bool:
    while p != None:
        if p.val == x:
            return True
        if p.val > x:
            return False
        p = p.next
    return False
