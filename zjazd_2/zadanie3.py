#sortowanie przez wybieranie
liczby = [8,3,4,0,2,1,5,6]

print("Przed: ", liczby)

for i in range(len(liczby)): #<-- drukuje coraz krótszą listę, bo i się zwiększa a to liczy od indeksu i do konca
    index_minimum = i
    print(liczby[1:])
    for j in range(i+1, len(liczby)):
        if liczby[j] < liczby[index_minimum]:
            index_minimum = j
    liczby[i], liczby[index_minimum] = liczby[index_minimum], liczby[i]
    print('i: ', i, 'liczby: ', liczby)

print("Po", liczby)

#liczby[0], liczby[4] = liczby[4], liczby [0] <--- zamienia je miejscami
