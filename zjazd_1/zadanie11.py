pozycja_x = int(input("Podaj pozycję x: "))
pozycja_y = int(input("Podaj pozycję y: "))

if pozycja_x < 0 or pozycja_y < 0 or pozycja_y > 100 or pozycja_x > 100:
    print("Gracz znajduje się poza planszą.")
elif pozycja_x < 10:
    print("Gracz znajduje się przy lewej krawędzi.")
elif pozycja_x > 90:
    print("Gracz znajduje się przy prawej krawędzi.")
elif pozycja_y < 10:
    print("Gracz znajduje się przy dolnej krawędzi.")
elif pozycja_y > 90:
    print("Gracz znajduje się przy górnej krawędzi.")
elif pozycja_x < 10 and pozycja_y < 10:
    print("Gracz znajduje się lewym dolnym rogu.")
elif pozycja_x < 10 and pozycja_y > 90:
    print("Gracz znajduje się lewym górnym rogu.")
elif pozycja_x > 90 and pozycja_y < 10:
    print("Gracz znajduje się prawym dolnym rogu.")
elif pozycja_x > 90 and pozycja_y < 10:
    print("Gracz znajduje się prawym górnym rogu.")
else:
    print("Gracz znajduje się w centrum planszy.")