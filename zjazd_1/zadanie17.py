li = []

while len(li) < 10:
    liczba = int(input("Podaj liczbę: "))
    li.append(liczba)
    ilo = str(input("Następna(t/n)? "))
    if ilo == "n":
        print("Liczę średnią.")
        break

av = sum(li) / len(li)
print(f"Twoja średnia: {av}")


