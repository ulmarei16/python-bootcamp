#liczenie samogłosek w podanym słowie
napis = input(str("Podaj napis: "))
vowel = 0

for i in napis:
    if i == "a" or i == "i" or i == "e" or i == "o" or i == "u" or i == "y":
        vowel += 1

print("Liczba samogłosek: " + str(vowel))