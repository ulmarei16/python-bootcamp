li = [5, 2, 1, 4, 3]
nw = None
nm = None

print(li)
indeksy = list(range(len(li)))

#sprawdzanie, która jest najwieksza, a ktora najmniejsza
for i in indeksy:
    if nm == None or li[i] < li[nm]:
        nm = i
    if nw == None or li[i] > li[nw]:
        nw = i
    #print(i) <--- wyświetlają proces
    #print(nw)
    #print(nm)

 # podmienianie wartości
if nm is not None and nw is not None:
    a = li[nw]
    li[nw] = li[nm]
    li[nm] = a

# lub li[nw], li[nm] = li[nm], li[nw]

print(li)


assert li == [1, 2, 5, 4, 3]