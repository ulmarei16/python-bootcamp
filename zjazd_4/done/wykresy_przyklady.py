#tabela kolorow: https://www.google.pl/imgres?imgurl=https://matplotlib.org/1.5.1/mpl_examples/color/named_colors.hires.png&imgrefurl=https://matplotlib.org/1.5.1/examples/color/named_colors.html&h=900&w=1100&tbnid=N8U4y3Ixxxi7JM:&q=matplotlib+colors+list&tbnh=160&tbnw=195&usg=AI4_-kT5WoxkI4FxOmhtT4Hsl6zqKnVZNA&vet=12ahUKEwibxqaa_t3eAhXmkYsKHYnlDpgQ9QEwAHoECAoQBg..i&docid=1U1xY3Tv6iw77M&sa=X&ved=2ahUKEwibxqaa_t3eAhXmkYsKHYnlDpgQ9QEwAHoECAoQBg

import matplotlib.pyplot as plt
import csv

#przezywalnosc procentowa
# dane = [70,18]
# index = ["kobiety","mezczyzni"]
# colours = ["r","g"]
#
# plt.bar(index,dane,color=colours) #bar chart
# plt.show()

with open("raport.csv") as f:
    dane = csv.reader(f, delimiter=",")
    srednie = []
    badani =[]
    for row in dane:
        if "Srednia" in row[0]: #<-- jak znalezc element w stringu
            srednie.append(float(row[1]))
            badani.append(row[0])

    # print(srednie)
    # print(badani)

colours=["teal","orchid"]
plt.bar(badani,srednie,color=colours)
plt.show()