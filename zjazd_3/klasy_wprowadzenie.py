x = 1
napis = "napis"
y = 1.2
dictionary = {}
def foo():
    pass
print(type(x),type(y),type(dictionary), type(napis), type(None), type(foo)) #pokazuje nam jakiej klasy są obiekty

print(dir(x))  # pokazuje metody dla klasy takiego obiektu

class Animal: #definition of a class
    nazwa = "fauna" #atrybut klasowy
    licznik = 0

    def __str__(self): #nadpisuje istniejącą już metodę
        return "Klasa animal"
    def __init__(self,gatunek,imie): # self refers to a particular instance
        self.gatunek = gatunek
        self.imie = imie
        self.zwieksz_licznik()
        self.stan = "nic nie robi"

    def idz(self):
        self.stan = "Idzie"

    def spi(self):
        self.stan = "Śpi"

    def stoj(self):
        self.stan = "Stój"

    @classmethod  #tworzenie funkcji wewnatrz klasowych
    def zwieksz_licznik(cls):
        cls.licznik += 1

class LeniweZwierzeta(Animal): #dziedziczenie z innej klasy
    def idz(self):
        self.stan = "Leży"
        print("Chyba żartujesz.")


azor = Animal("canis familiaris", "azor") #creates an instance of a class
rudolf = Animal("ragnifer tarandus", "rudolf")
print(type(azor))
print(dir(azor))
print(azor.gatunek) #wypisuje atrybut
print(rudolf.imie)
print(azor.nazwa)

azor.gatunek = "felis catus" #zmiana atrybutu danego instance
print(azor.gatunek)




print(azor.stan)
azor.idz()
print("Stan zwierzaka: ", azor.stan)

garfield = LeniweZwierzeta("felis catus","garfield")
LeniweZwierzeta.idz(garfield)
garfield.idz()
print("Stan zwierzaka:", garfield.stan)