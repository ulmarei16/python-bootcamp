liczniki_liter = {}
napis = input("Podaj dowolny napis: ")

# #sposob 1 dla prostaka <--- działa
# for litera in napis:
#     if litera in liczniki_liter:
#         liczniki_liter[litera] = liczniki_liter[litera] + 1
#     else:
#         liczniki_liter[litera] = 1

#sposób 2 ładniejszy  <--- działa
for litera in napis:
    liczniki_liter[litera] = liczniki_liter.get(litera, 0) + 1 # <--- get sprawdzaczy dany klucz istnieje. jeżeli istnieje to dodaje wartość, jak nie istnieje to dodajew klucz i wartość


print("Ile razy występuje każdy znak: ")
for znak in liczniki_liter:
    print("litera " + str(znak) + " wystąpiła " + str(liczniki_liter[znak]) + " razy")