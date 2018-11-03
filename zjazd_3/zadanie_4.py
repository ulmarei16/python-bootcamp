class Product:
    def __init__(self,ID,nazwa,cena):
        self.cena = cena
        self.nazwa = nazwa
        self.ID = ID

    def drukuj_produkt(self):
        print("Produkt: ", self.nazwa, ", id: ", self.ID, ", cena: ", self.cena,"PLN")

class Basket(object):
    def __init__(self):
        self.products = []

    def add_product(self,product,amount):



def test_Basket():
    basket = Basket()
    product = Product(1, "woda", 10.00)
    basket.add_product(product,5)
    assert basket.count_total_price() == 50.0
    assert basket.generate_report() == """Produkty w koszyku 
                                       - Woda (1), cena 10.00 x 5 
                                       W sumie: 50.00"""


