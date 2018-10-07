li1 = list() # tworzy pustą listę
li2 = [] # tworzy pustą listę
li3 = [1,2,3,4]
li4 = list((1,2,'a'))

#dodawanie do listy
li4.append('a') #doda na koniec listy jeden element
print(li4)

li4.insert(2, 'a') #doda obiekt na pozycji 2 (pozycje są liczone od 0_)

li4.extend(li3) #połączy elementy

li4.pop() #usówa ostatni element

li4.pop(3) #usówa element 3

len(li3) #liczy elementy

for zmiennatymczas in li3:
    #zrób coś ze zmienną tymczasową, która przyjmuje wartość każdego elementu
    print(zmiennatymczas **2)

for licznik, zmiennatymczas in enumerate(li3, 2)
    print(licznik, zmiennatymczas, zmiennatymczas **2)



range <-- zasięg
for i in range(10) <-- zasięg od 0 do 9
         range(1, 50, 5) <-- zasięg od zero do 49 i co pięć