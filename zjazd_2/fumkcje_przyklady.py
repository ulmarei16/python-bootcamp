# przjęło się, że funkcje nazywamy jak zmienne, małymi literami, rozdzielamy podkreslnikami
# to_jest_funkcja
# w nawiasach okrągłych podajemy jakąś ilość paramteró, kótre będą obsługiwane przez funkcję może być ich zero
#___________________________________________________________

def drukuj_linie():
    print("_"*40)
#_______________________________________________________

def przyjmij_wartosc_wpisana():
    wartosc = input('podaj wartosc: ')
    return wartosc

x = przyjmij_wartosc_wpisana()
print(x)

#______________________________________________________

def sumator(a,b):
    return a + b

#____________________________________________________

def sumator_dwa(a):
    return sum(a)

a = [1,2,3,4,5,6,7]

print(sumator_dwa(a))

#____________________________________________________

def zwroc_sume_zdefiniowanej_listy():
    b = 1
    print("poziom 1", locals()) #<--- locals to zmienne z wewnatrz funkcji, jeżeli funkcja nie ma zmiennych lolkalnych szuka ich na wyzszym posiomie
    print("poziom 2", globals())
    #a = [5,6,7]
    a.append(b)

    def funkccja_wewnetrzna():
        c = 1
        print("poziom 2", locals())
        print("poziom 2", globals())
        print("b", b)
    return sum(a)

print("poziom 0",locals())
print("poziom 0",globals())
print(zwroc_sume_zdefiniowanej_listy())

#_________________________________________________
def kalkulator(a,b,operacja="+",opis=""): #<----- działa na 2 liczbach i domyslnie je sumuje
    if opis:
        print(opis)
    if operacja == "+":
        return a+b
    elif operacja == "-":
        return a-b #<------ funkcja konczy się tam gdzie jest return, nic po return sue nie dzieje


print(kalkulator(1,2))
print(kalkulator(1,2,"-"))
print(kalkulator(1,2,"-","Odejmowanie 2 liczb"))
print(kalkulator(1,2, opis="Dodawanie 2 liczb"))
