napis = "Ala ma kota"
#        012345678910  <- index elementów  napisu

print(napis[2])
print(napis[4])

#for litera in napis:
    #print(litera)


print(napis[0:4]) # pokazuje od elementu 0 do 4

print(napis[0:10:2]) # pokaż co drugi element

print(napis[-2]) #pokaż 2 od końca

#tupla tuple
ala = ('A', 'l', 'a', '', 'm', 'a')
print(ala[0:5])

print('a' in ala) #<-- sprawdza czy dany element wystpępuje w tupli


type(ala)  #mówi jakim obiektem jest "ala"

a = (1, 2, (3, 4), 'a', 'b', 'napisy')
1 in a #<-- sprawdza czy dany element jest w tupli

# [] to operator wybierania
a[2] #<-- wybiera element 2
a[2][1] #<--- wybiera element 1 z elementu 2

# [:] okresla zakres  [:3] weź od zera do 3
# [::x] x określa co ile elementów
# [-x] służy do liczenia elementów od konca

# 'There's a snake in my boot!'

#This code breaks because Python thinks the apostrophe in 'There's' ends the string. We can use the backslash to fix the problem, like this:

#'There\'s a snake in my boot!'

