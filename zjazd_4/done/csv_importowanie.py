import csv

with open("titanic_train.csv") as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    # dlugosci = set()
    # for row in data:
    #     #print(row)
    #     dlugosci.add(len(row))

    dlugosci = {}
    for row in data:
        dlugosci[row[1]] = dlugosci.get(row[1],0)+1

print(dlugosci)