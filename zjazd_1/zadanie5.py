miastoA = input("Miasto A: ")
miastoB = input("Miasto B: ")
dystans = float(input(f"Dystans {miastoA}-{miastoB}: "))
cena = float(input("Cena paliwa: "))
spalanie = float(input("Spalanie na 100km: "))

koszt = int(((dystans/100) * spalanie) * cena)

output = f"""
    Miasto A: {miastoA}
    Miasto B: {miastoB}
    Dystans: {dystans}
    Cena paliwa: {cena}
    Spalanie na 100km: {spalanie}
    
    Koszt przejazdu z {miastoA} do {miastoB} to {koszt} PLN
"""

print(output)