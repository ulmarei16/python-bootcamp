def starting_location():
    from random import randint
    x = randint(1, 10)
    y = randint(1, 10)
    return x, y

# def podaj_ruch():
#     ruch = input("Jak chcesz się ruszyć (a = lewo, w = góra, d = prawo, s = dół)?  ")
#     return ruch

def minimalna_liczba_kroków(gracz_x, skarb_x, gracz_y, skarb_y):
    return abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)

def zmiana_pozycji_gracza(gracz_x,gracz_y):
    ruch = ruch.lower()
    if ruch == "a":
        gracz_x = gracz_x - 1
    if ruch == "d" :
        gracz_x = gracz_x + 1
    if ruch == "w":
        gracz_y = gracz_y + 1
    if ruch == "s":
        gracz_y = gracz_y - 1
    return gracz_x, gracz_y


skarb_x, skarb_y = starting_location()
gracz_x, gracz_y = starting_location()
#podaj_ruch()