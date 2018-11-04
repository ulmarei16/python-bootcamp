# kommentowanie bloku, zaznaczamy blok, ctrl + /

my_dict = {
    "pierwsza": "a",
    "druga": "b"
}
print(my_dict['druga'])

print(type(my_dict)) #drukuje klasę obiektu

print(my_dict.items()) # pokazuje co jest w środku w parach klucz i wartości do niego przypisane

print(my_dict.keys()) #drukuje ty6lko klucze

print(my_dict.values()) #drukuje tylko wartości

my_dict ['trzecia'] = 'c' #dodaje nowy klucz i wartość

d2 = dict()
d2 = dict([('a',1) ('b',2)])

produkt1 = {'nazwa': "Koper", "cena": 3}
produkt2 = {'nazwa': "Kasza", "cena": 1.99}
produkty = [produkt1, produkt2]

print("produkty")
for p in produkty:
    print (p("nazwa"))

for k in produkty:
    print ()

#pseudo dodawanie słowników
a = {"a" : 1, "b" : 2}
b = {"b" : 3, "d" : 4}

print(a)
print(b)

a.update(b)
print(a)

from collections import OrderedDict, defaultdict

