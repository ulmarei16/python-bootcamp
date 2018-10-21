def pobierz_dane():
    miastoA = input("Miasto A: ")
    miastoB = input("Miasto B: ")
    dystans = float(input(f"Dystans {miastoA}-{miastoB}: "))
    cena = float(input("Cena paliwa: "))
    spalanie = float(input("Spalanie na 100km: "))
    return dystans, cena, spalanie, miastoA, miastoB

def policz_koszt(dystans,cena,spalanie,mistoA,miastoB):
    koszt = int(((dystans / 100) * spalanie) * cena)
    return koszt

def drukuj_koszt(dystans,cena,spalanie,miastoA,miastoB):
    output = f"""
        Miasto A: {miastoA}
        Miasto B: {miastoB}
        Dystans: {dystans}
        Cena paliwa: {cena}
        Spalanie na 100km: {spalanie}

        Koszt przejazdu z {miastoA} do {miastoB} to {koszt} PLN
    """
    return print(output)


dane = pobierz_dane()
print(dane)
print(type(dane))
koszt = policz_koszt(*dane) #<--- gwizzdka rozpakuje kolekcje
print(drukuj_koszt(*dane))

def test_policz_koszt():
     assert policz_koszt(100,5,5,"a","b") == 25
