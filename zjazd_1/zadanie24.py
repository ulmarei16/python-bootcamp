sklep = {
    "jabłka" : 2,
    "gruszki" : 3,
    "śliwki" : 5
}
cena_za_kg = 0

print("Dostępne produkty i ceny za kilogram: ")
print(sklep)

towar = input(str("Podaj nazwę towaru, który chesz kupić: "))
waga = input(str("Podaj ile towaru chcesz kupić (w kg): "))

for x in sklep:
    if x == towar:
        cena_za_kg = sklep[x]

do_zaplaty = cena_za_kg * int(waga)
print("Musisz zapłacić: " + str(do_zaplaty))

