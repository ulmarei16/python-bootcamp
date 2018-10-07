a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a[1]) #drukuje pierwszy element
assert 2 == a[1] # "assert" sprawdza, czy to się zgadza
print(a[-2]) #drukuje przedostatni element
print(a[2:7]) #drukuje elementy od 3 do 8
print(a[::3]) #drukuje co 3 element
print(a[::-2]) # drukuje co 2 element od konca
print(len(a)) #pokazuje długość tupli

x = tuple() #tworzy pustą tuplę