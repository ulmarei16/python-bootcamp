import ast

with open("obiekty_tekstowe.txt") as e:
    obiekty = e.read()
    obiekty = ast.literal_eval(obiekty)
    print(type(obiekty))
    print(obiekty)

    