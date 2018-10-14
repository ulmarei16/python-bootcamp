a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
operacja = str(input("Podaj rodzaj operacji: "))
dodawanie = a + b
odejmowanie = a - b
mnozenie = a * b
dzielenie = a / b


if operacja == "+":
    print("Wynik: {dodawanie}")
elif operacja == "-":
    print("Wynik: {odejmowanie}")
elif operacja == "*":
    print("Wynik: {mnozenie}")
elif operacja == "/":
    if b == 0:
        raise ValueError ("Dla tej operacji druga liczba musi być inna niż zero")
    print("Wynik: {dzielenie}")
else:
    #print("Nieznane działanie.")
    raise ValueError ("Nieprawidłowa wartość parametru.")