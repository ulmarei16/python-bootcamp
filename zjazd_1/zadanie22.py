#liczenie samogłosek w podanym słowie
napis = input(str("Podaj napis: "))
SAMOGLOSKI ='aiueoy'
vowel = 0

for i in napis:
    #if i == "a" or i == "i" or i == "e" or i == "o" or i == "u" or i == "y":
    if i in SAMOGLOSKI:
        vowel += 1

print("Liczba samogłosek: " + str(vowel))