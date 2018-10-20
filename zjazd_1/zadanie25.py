napis_dict = {}
napis = str(input("Podaj dowolny napis: "))
ilo_znaku = 0

for x in napis:
    if x in napis_dict:
        napis_dict[x] += 1
    else:
        napis_dict[x] = 1

print (napis_dict)


