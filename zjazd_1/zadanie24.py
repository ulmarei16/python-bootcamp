sklep = {
    "jabłka" : 2,
    "gruszki" : 3,
    "śliwki" : 5
}
magazyn = {
    "jabłka" : 10,
    "gruszki" : 10,
    "śliwki" : 10
}
cena_za_kg = 0
za_towar = 0
do_zaplaty = 0

while True:
    print("-"*40)
    print("Dostępne produkty i ceny za kilogram: ")
    #print(sklep)

    for produkt in sklep:
        cena = sklep[produkt]
        print(f'- {produkt} - {cena} PLN') #bardziej elegancka wersja
    komenda = input("Co chcesz zrobić: [z] = zakupy, [k] koniec:")
    if komenda == "k":
        break


    towar = input(str("Podaj nazwę towaru, który chesz kupić: "))
    if towar not in sklep:
        print("Nie ma takiego produktu.")
        continue
    waga = float(input("Podaj ile tego towaru chcesz kupić (w kg): "))
    if magazyn[towar] < waga:
            print(f"Mamy za mało [{towar}].")
            continue
    magazyn[towar] = magazyn[towar] - waga

    #if towar in koszyk: <----------- żeby m,ożna było 2 razy kupić
        #koszyk[towar] = coś plus coś???????????????????
    #else:
        #koszyk = coś

    #to jest żle
    # for x in sklep:
    #     if x == towar:
    #         cena_za_kg = sklep[x]
    #
    # za_towar = cena_za_kg * waga
    # do_zaplaty += za_towar

# drugi sposob
# waga2 = float(input("Ile chcesz tego kupić: "))
#
# cena = sklep[towar]
# koszt = waga2 * cena
#


# trzeba dodac dodawanie nowych produktów więcej towaru do magazynu i drukowanie paragonu

#do_zaplaty = cena_za_kg * float(waga)
print("="*40)
print("Do zapłaty: " + str(do_zaplaty))

