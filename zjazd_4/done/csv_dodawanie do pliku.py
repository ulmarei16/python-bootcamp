import csv

#liczymy przezywalnosc %, ogolu, kobiet i mezczyzn
#plik trzeba otwierac ponownie po kazdym for, bo inaczej nie dziala, nie chce nastewpnego for robic
wyniki = []

with open("titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")

    dlugosci = {}
    for row in data:
        dlugosci[row["Survived"]] = dlugosci.get(row["Survived"], 0) + 1
    #print(dlugosci)
    #ogolem przezywalnosc
    przezylo = dlugosci["1"]
    zginelo = dlugosci["0"]
    wyniki.append(("Przeżylo z ogolu ", 100*przezylo/(przezylo+zginelo)))

with open("titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    kobiety = {}
    mezczyzni= {}
    for row in data:
        if row["Sex"] == "female":
             kobiety[row["Survived"]] = kobiety.get(row["Survived"], 0) + 1

    przezylo = kobiety["1"]
    zginelo = kobiety["0"]
    wyniki.append(("Przeżylo z kobiet ", 100 * przezylo / (przezylo + zginelo)))

with open("titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    mezczyzni = {}
    for row in data:
       if row["Sex"] == "male":
          mezczyzni[row["Survived"]] = mezczyzni.get(row["Survived"], 0) + 1

    przezylo = mezczyzni["1"]
    zginelo = mezczyzni["0"]
    wyniki.append(("Przeżylo z mezczyzn ", 100 * przezylo / (przezylo + zginelo)))


with open("titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")

    how_many_women= 0
    sum_woman_age =0

    for row in data:
        if row["Sex"] == "female" and row["Age"] != "":
            how_many_women += 1
            sum_woman_age += float(row["Age"])

    wyniki.append(("Srednia wieku kobiet ", sum_woman_age/how_many_women))

with open("titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")

    how_many_men = 0
    sum_men_age = 0
    for row in data:
       if row["Sex"] == "male" and row["Age"] != "":
           how_many_men += 1
           sum_men_age += float(row["Age"])

    wyniki.append(("Srednia wieku mezczyzn ", sum_men_age / how_many_men))

print(wyniki)

with open("raport.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(wyniki)



