#kwadraty = [x**2 for x in range (1,101)]   <---------- wersja skrócona tego co na dole

#kwadraty = []
#for x in range (1, 101):
#    kwadraty.append(x**2)


print([i/10 for i in range(11)])

print({(i, i**2, i**3) for i in range(-10,10)})

zbior_napisow = {'abc','blepleple','ala ma kota','super','costam costam'}
print({x:len(x) for x in zbior_napisow})
print([x for x in range(1,101) if x%3==0])