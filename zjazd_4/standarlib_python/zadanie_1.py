import json

try:   #<--- próbuje coś robić
    with open("pracownicy.json") as f:
        pracownicy = json.load(f)

except FileNotFoundError: #<-- jeżeli pojawi się błąd to rób to
    pracownicy= []

dane_pracownika = {}
#nr_pracownika = 0

co_zrobic = input("Co chcsz zrobić? [d - dodaj, w - wypisz]: ")

if co_zrobic == "d":
    # nr_pracownika  += 1
    # dane_pracownika ["Numer"] = nr_pracownika
    dane_pracownika ["Imie"] = input("Imie: ")
    dane_pracownika ["Nazwisko"] = input("Nazwisko: ")
    dane_pracownika ["Rok urodzenia"] = int(input("Rok urodzenia: "))
    dane_pracownika ["Pensja"] = float(input("Pensja: "))
    pracownicy.append(dane_pracownika)
    with open("pracownicy.json", "w") as f:
        f = json.dump(pracownicy,f)
        #print(json.dumps(pracownicy))

elif co_zrobic == "w":

    print("Pracownicy:")
    for i,pracownik in enumerate(pracownicy, start=1):
        print("- [", i,"] ",pracownik["Imie"]," ", pracownik["Nazwisko"]," - rok: ",pracownik["Rok urodzenia"],", pensja: ",pracownik["Pensja"], " PLN")

else:
    print("Niepoprawne polecenie.")




