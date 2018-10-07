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

li3
