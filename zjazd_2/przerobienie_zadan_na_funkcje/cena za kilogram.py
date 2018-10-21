def licz_naleznosc(cena,waga):
    # naleznosc = cena * waga
    # return naleznosc
    return cena * waga


def podaj_naleznosc(cena,waga):
    rachunek = f""" 
        cena: {cena}
        waga: {waga}
        należność: {licz_naleznosc(cena,waga)}
    """
    return print(rachunek)


def test_licz_naleznosc():
    assert licz_naleznosc(10,2.5) == 25

def test_podaj_naleznosc():
    assert podaj_naleznosc(10,2.5) == print(f""" 
    cena: {10}
    waga: {2.5}
    należność: {25}
""")
