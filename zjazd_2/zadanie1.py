napis_dict = {}
napis = input(str("Podaj dowolny napis: "))


for x in napis:
    napis_dict[x] = napis_dict[x] + 1

print("Ile razy występuje każdy znak: ")
for znak in napis_dict:
    print napis_dict.get()