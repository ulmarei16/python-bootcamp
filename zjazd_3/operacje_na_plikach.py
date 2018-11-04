#stary sposob wywolywania plilkow
file = open("dane/emails.txt")
print(file.read()) #<-- wypisuje się co jest w pliku
file.close()


#nowy sposob, auto zamyka, bo jest wciecie
with open("dane/emails.txt") as f:
    print(f.read())

#tworzenie nowgo pliku
with open("dane/nowy_plik.txt", 'w', encoding='utf8') as f: #<---- 'w' powoduje że nadpisuje to co bylo wczesniej, 'x' tworzy nowy plik i do zaczynania pisania
    f.write("Jakiś tekst")  #<=== wpisuje dane do pliku

with open("dane/nowy_plik.txt", "a", encoding='utf8') as f:  # <---- 'a' pozwala na otworzenie i dopisanie czegoś
    f.write("Jakiś tekst")  # <=== wpisuje dane do pliku


import sys
nazwa_pliku = sys.argv[1] #<--- sys.argv to taka lista ktora zbiera toco urzytkownik poda na linii polecen, index 0 na tej liscie to nazwa pliku ktorego to dotyczy
with open(nazwa_pliku) as f: