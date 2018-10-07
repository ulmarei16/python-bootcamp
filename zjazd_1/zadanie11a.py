pozycja_x = int(input("Podaj pozycję x: "))
pozycja_y = int(input("Podaj pozycję y: "))

wymiar_x = int(input("Podaj wymiar x: "))
wymiar_y = int(input("Podaj wymiar y: "))

if pozycja_x < 0 or pozycja_y < 0 or pozycja_y > wymiar_y or pozycja_x > wymiar_x:
    print("Gracz znajduje się poza planszą.")
elif pozycja_x < 0.1 * wymiar_x and pozycja_y < 0.1 *wymiar_y:
    print("Gracz znajduje się lewym dolnym rogu.")
elif pozycja_x < 0.1 * wymiar_x and pozycja_y > wymiar_y:
    print("Gracz znajduje się lewym górnym rogu.")
elif pozycja_x > 0.9 * wymiar_x and pozycja_y < 0.1 * wymiar_y:
    print("Gracz znajduje się prawym dolnym rogu.")
elif pozycja_x > 0.9 * wymiar_x and pozycja_y < 0.1 * wymiar_y:
    print("Gracz znajduje się prawym górnym rogu.")
elif pozycja_x < 0.1 * wymiar_x:
    print("Gracz znajduje się przy lewej krawędzi.")
elif pozycja_x > 0.9 * wymiar_x:
    print("Gracz znajduje się przy prawej krawędzi.")
elif pozycja_y < 0.1 * wymiar_y:
    print("Gracz znajduje się przy dolnej krawędzi.")
elif pozycja_y > 0.9 * wymiar_y:
    print("Gracz znajduje się przy górnej krawędzi.")
else:
    print("Gracz znajduje się w centrum planszy.")