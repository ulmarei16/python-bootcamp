#liczenie liter w nawiasie <>
napis = input(str("Podaj napis i umieść jedno słowo w nawiasie <> : "))

il_nawias = 0
il_nawias2 = 0

for i in napis:
    if i == "<":
        nawias1 = napis.index(i)
        il_nawias += 1
    if i == ">":
        nawias2 = napis.index(i)
        il_nawias2 += 1

if il_nawias > 1 or il_nawias2 > 1:
    print("miał być tylko jeden nawias")
else:
    il_lit = nawias2 - nawias1 - 1
    print ("Ilość znaków w nawiasie: " + str(il_lit))

#nie wiem jak uwarunkować, że jest tylko jeden nawias

#sposob 2
czy_miedzy_nawias = False
licznik = 0

for znak in napis:
    if znak == "<":
        czy_miedzy_nawias = True
    elif znak == ">":
        czy_miedzy_nawias = False
    elif czy_miedzy_nawias:
        licznik += 1

print(licznik)
#nie mam pojęcia jak sposob 2 dziala XD
