#from random import randint <-- losowanie przypadkowej liczby ze zbioru
# x = randint (0, 10) <-- losuje jedną z 10
# i = 0
    # while i <= 10
        #x = randint (0, 10)
        #print(x)
        #i = i +1

# abs(7-9) <--- równa się 2
# abs(9-7) <-- równa się 2

#gra

from random import randint
#losuje polozenie skarbu
skarb_x = randint(1, 10)
skarb_y = randint(1, 10)

#losuje polozenie gracza
gracz_x = randint(1, 10)
gracz_y = randint(1, 10)

# while skarb_x == gracz_x and skarb_y == gracz_x:
    #gracz_x = randint(1, 10)
    #gracz_y = randint(1, 10)

#minimalna ilosc krokow do skarbu
minkrok = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)

krok = 0

#poruszanie się gracza
while True:
    ruch = input("Jak chcesz się ruszyć (a = lewo, w = góra, d = prawo, s = dół)?  ")
    if ruch == "a":
        gracz_x = gracz_x - 1
        krokpo = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
        if krokpo > minkrok:
            print("Zimno")
        if krokpo < minkrok:
            print("Ciepło")
        if minkrok == 0:
            print("Wygrana")
            break
    if ruch == "d" :
        gracz_x = gracz_x + 1
        krokpo = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
        if krokpo > minkrok:
            print("Zimno")
        if krokpo < minkrok:
            print("Ciepło")
        if minkrok == 0:
            print("Wygrana")
            break
    if ruch == "w":
        gracz_y = gracz_y + 1
        krokpo = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
        if krokpo > minkrok:
            print("Zimno")
        if krokpo < minkrok:
            print("Ciepło")
        if minkrok == 0:
            print("Wygrana")
            break
    if ruch == "s":
        gracz_y = gracz_y - 1
        krokpo = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
        if krokpo > minkrok:
            print("Zimno")
        if krokpo < minkrok:
            print("Ciepło")
        if minkrok == 0:
            print("Wygrana")
            break
    if gracz_x < 1 or gracz_y < 1 or gracz_x > 10 or gracz_y > 10:
            print("Przegrana: jesteś poza planszą.")
            break
    minkrok = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    krok = krok + 1


#ilość kroków wykonanych w ciągu gry
print(f"Ilość wykonanych kroków: {krok}")
