def podzielne_przez_2(x):
    return x%2 == 0

print(podzielne_przez_2(12))
print(podzielne_przez_2(11))

y = lambda x: x%2 == 0
print(y(4))
print(y(5))

def wieksza_niz(x):
    if x>7:
        return True
    else:
        return False

def wybierz(dane,warunek):
    out = []
    for element in dane:
        if warunek(element):
            out.append(element)
        return out

def podzielna_przez_3(x):
    return x % 3 == 0

lista = [1,2,3,4,5,6,7,89,99]
print(wybierz(lista, podzielne_przez_2))
print(wybierz(lista, wieksza_niz))
print(wybierz(lista, lambda x: x%3 == 0))
print(wybierz(lista, podzielna_przez_3))

