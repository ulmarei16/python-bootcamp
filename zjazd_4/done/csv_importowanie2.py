import csv

#liczymy przezywalnosc %, ogolu, kobiet i mezczyzn
#plik trzeba otwierac ponownie po kazdym for, bo inaczej nie dziala, nie chce nastewpnego for robic

with open("titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")

    dlugosci = {}
    for row in data:
        dlugosci[row["Survived"]] = dlugosci.get(row["Survived"], 0) + 1
    #print(dlugosci)
    #ogolem przezywalnosc
    przezylo = dlugosci["1"]
    zginelo = dlugosci["0"]
    print("Przeżylo z ogolu ", round(100*przezylo/(przezylo+zginelo), 2))

with open("titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    kobiety = {}
    mezczyzni= {}
    for row in data:
        if row["Sex"] == "female":
             kobiety[row["Survived"]] = kobiety.get(row["Survived"], 0) + 1

    przezylo = kobiety["1"]
    zginelo = kobiety["0"]
    print("Przeżylo z kobiet ", round(100 * przezylo / (przezylo + zginelo), 2))

with open("titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    mezczyzni = {}
    for row in data:
       if row["Sex"] == "male":
          mezczyzni[row["Survived"]] = mezczyzni.get(row["Survived"], 0) + 1

    przezylo = mezczyzni["1"]
    zginelo = mezczyzni["0"]
    print("Przeżylo z kobiet ", round(100 * przezylo / (przezylo + zginelo), 2))

with open("titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")

    how_many_women= 0
    sum_woman_age =0
    # unique_age_values = set()
    # for row in data:
    #     unique_age_values.add(row["Age"])

    for row in data:
        if row["Sex"] == "female" and row["Age"] != "":
            how_many_women += 1
            sum_woman_age += float(row["Age"])

    print ("Srednia wieku kobiet: ", sum_woman_age/how_many_women)

with open("titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")

    how_many_men = 0
    sum_men_age = 0
    for row in data:
       if row["Sex"] == "male" and row["Age"] != "":
           how_many_men += 1
           sum_men_age += float(row["Age"])

    print("Srednia wieku mezczyzn: ", sum_men_age / how_many_men)








    # survived_male = {}
    # survived_fem = {}
    # for row in data:
    #     if row["Sex"] == "male":
    #         survived_male[row["Survived"]] = survived_male.get(row["Survived"], 0) + 1
    #     if row["Sex"] == "female":
    #         survived_fem[row["Survived"]] = survived_fem.get(row["Survived"], 0) + 1
    #
    # print(survived_fem)
    # print(survived_male)
    # źle




