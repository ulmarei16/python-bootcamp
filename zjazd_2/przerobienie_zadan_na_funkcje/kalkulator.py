def podaj_dane():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    operacja = str(input("Podaj rodzaj operacji (+,-,*,/): "))
    return a, b, operacja

def policz(a,b,operacja):
    if operacja == "+":
        dzialanie = a + b
    elif operacja == "-":
        dzialanie = a - b
    elif operacja == "*":
        dzialanie = a * b
    elif operacja == "/":
        dzialanie = a / b
    return dzialanie

def pokaz_wynik(policz):
    dane = podaj_dane()
    try:
        wynik = policz(*dane)
    except ValueError:
        wynik = "nidozwolan operacja"
    return wynik


podaj_dane()
print(pokaz_wynik())