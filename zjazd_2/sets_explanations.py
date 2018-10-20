zbior = {1,2,3,4} # <--- wyglądają jak klucze ze słownika, są to elementy unikatowe

print(zbior)
zbior.add("a")
print(1 in zbior) #<--- pokaże wartośc true or flase, w zależności czy to tam jest

a = {1,2,3}
b = {3,4,5}

print(a | b) #<--- suma zbiorów
print(a.union(b))
print(a - b) #<--- różnica - usuwa wspólne elementy
print(a.difference(b))
print(a & b) #<--- część wspólna
print(a.intersection(b))
print(a ^ b) #<--- to co nie jest wspólne
print(a.symmetric_difference(b))

print(dir(a))

print(set(range(1,10))) #<--- da liczby od 1 do 9