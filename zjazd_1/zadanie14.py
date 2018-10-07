#znajdź max i min liczbę i pozwol uzytkownikowi zakonczyc program

max_ = None
min_ = None

while True:
    wprowadzone = input("Podaj liczbę lub wpisz KONIEC, żeby zakoczyć: ")

    #if wprowadzone != int:
  #          if wprowadzone.lower() = "koniec":
   #             break
    #        else:
     #           print("Podaj prawidłowe dane.")
    if wprowadzone.lower() = "koniec":
        break
    else:
        liczba = int(wprowadzone)

        if max_ is None or liczba > max_: # Przy None używamy "is" zamiast "=="
            max_ = liczba
        if min_ is None or liczba < min_:
            min_ = liczba

print(f"Maksymalna liczba: {max_}.")
print(f"Minimalna liczba: {min_}.")

if not max_:
    print("Nie wprowadzono danych.")


# a = "Ala ma kota"
# dir (a) <--- pokazuje informacje o a np "metody" czyli np kapitalizacja, pozycja it
# a.lower <-- powoduje że a całe z małej litery
# a.upper <-- powodzuje, że całość wielką literą
# a.title <-- powoduje, że zaczyna się z wielkich liter
# tego jest dużo dużo więcej
