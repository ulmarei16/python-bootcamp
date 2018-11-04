class Product:
    def __init__(self,ID,name,price):
        self.price = price
        self.name = name
        self.ID = ID

    # def drukuj_produkt(self):
    #     print(self.name, " (", self.ID, ") cena: ", self.price)


class BasketEntry:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    def count_price(self):
        return self.product.price * self.quantity

    # def drukuj_produkt(self):
    #     print(self.product.name, " (",self.product.ID,") cena: ", self.product.price)

class Basket(object):
    def __init__(self):
        self.entries = []

    def __str__(self):
        return "Basket"

    def add_product(self, product, quantity):
        basket_entry = BasketEntry(product, quantity)
        self.entries.append(basket_entry)

    def count_total_price(self):
        product_total = 0
        for entry in self.entries:
            product_total += entry.count_price()
        return product_total

    # def generate_report(self): <--- żle
    #     print("Produkty w koszyku")
    #     for entry in self.entries:
    #         print("- ", entry.drukuj_produkt(), " x ", entry.quantity)
    #     print("W sumie:", self.count_total_price())

    def generate_report(self):
        total_price = self.count_total_price()
        products = ""
        for entry in self.entries:
            products += f"- {entry.product.name}({entry.product.ID}), cena: {entry.product.price} x {entry.quantity}\n"
        output = """Produkty w koszyku
{}W sumie:{}"""
        return output.format(products, total_price)

def test_Basket():
    basket = Basket()
    product = Product(1, "woda", 10.00)
    basket.add_product(product,5)
    assert basket.__str__() == "Basket"

def test_add_product():
    basket = Basket()
    product = Product(1, "woda", 10.00)
    basket.add_product(product, 5)
    assert basket.count_total_price() == 50.0


def test_basket_generate_report():
    basket = Basket()
    product = Product(1, "woda", 10.00)
    basket.add_product(product, 5)
    assert basket.generate_report() == """Produkty w koszyku
- woda (1), cena 10.0 x 5
W sumie: 50.0"""


