#rekurencja to znaczy ze funkcja wola sama siebie

#10! = 1 * 2 * 3 ... do 10

def silnia(liczba):
    if liczba == 0:
        return 1
    return liczba*silnia(liczba-1)

print(silnia(10))