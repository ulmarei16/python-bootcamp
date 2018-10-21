def przywitajsie(): #<--- definiuję funkcję i ją nazywam
    print("Hello")
    return 1

print(przywitajsie) #<---- wywoływanie funkcji
print(type(przywitajsie)) #<---- wywoływanie funkcji

x = przywitajsie()

print(x)
print(type(x))

def przywitajsie(imie): #<--- definiuję funkcję i ją nazywam
    print("Hello ", imie)

przywitajsie("Zosia")

lista_imion = ["Zosia","Kasia"]
for imie in lista_imion:
    przywitajsie(imie)


def przywitajsie(imie, wiek, wzrost, waga):  # <--- definiuję funkcję i ją nazywam
    print("Hello ", imie)



lista_osob = [{
    'imie': 'Kasia',
    'wiek': 90,
    'wzrost': 160,
    'waga': 50
},
    {'imie': Zosia,
    'wiek': 15,
    'wzrost': 120,
    'waga': 30,
}]

for osoba in lista_osob:
    przywitajsie(osoba['imie'],osoba['wiek'],osoba['wzrost'],osoba['waga'])

for imie in lista_imion:
    przywitajsie(imie)

def foo2(cena, *args): #<--- *args = dowolna ilośćargumentów, wpisujemy to na koncu
    print("args", args)
    print("cena", cena)

x = ["tekst $cena","text $cena","tekst1"]
foo2(*x, cena=10)

#**kwargs <--- tworzą słownik

for k in kwargs:
    text = text.replace(f'${k}',str(kwargs[k]))

"\n".join(out)  #<--------- łączy elementy listy z nowa linia