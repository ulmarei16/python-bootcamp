class Produkt:
    def __init__(self,cena,nazwa,ID):
        self.cena = cena
        self.nazwa = nazwa
        self.ID = ID

    def drukuj_produkt(self):
        print("Produkt: ", self.nazwa, ", id: ", self.ID, ", cena: ", self.cena,"PLN")


produkt = Produkt(10.99, "woda", 1)
produkt.drukuj_produkt()

def test_produkt():
    produkt = Produkt(10.99,"woda",1)
    assert produkt.cena == 10.99
    assert produkt.nazwa == "woda"
    assert produkt.ID == 1

    assert hasattr(produkt,"cena") #sprawdza czy dany obiekt ma jakiś atrybut