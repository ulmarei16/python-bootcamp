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
