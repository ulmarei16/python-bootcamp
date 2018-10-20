zbior = set()
doodatnie_do_stu = set(range(0, 101, 2))

x = (input("Podaj liczbę całkowitą (wpisz [k] jeżeli chcesz skończyć): "))

while x != "k":
        x = int(x)
        zbior.add(x)
        x = (input("Podaj liczbę całkowitą (wpisz <stop> jeżeli chcesz skończyć): "))




dodatnie = (zbior & doodatnie_do_stu)
print(f"Ilość podanych unikalnych liczb dodatnich: {len(dodatnie)}")