wysokosc = float(input("podaj wysokość w centymetrach: "))
glebokosc = float(input("podaj głębokość w centymetrach: "))
szerokosc = float(input("podaj szewrokość w centymetrach: "))
objetosc = wysokosc * szerokosc * glebokosc

print(objetosc)

if objetosc > 1000:
    print("objetość większa niż 1000cm3")
else:
    print("objętość mniejsza lub równa 1000cm3")