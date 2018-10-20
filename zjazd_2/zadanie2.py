zbior = set()
doodatnie_do_stu = set(range(2, 101, 2))

# x = (input("Podaj liczbę całkowitą (wpisz [k] jeżeli chcesz skończyć): "))
#
# while x != "k":
#         x = int(x)
#         zbior.add(x)
#         x = (input("Podaj liczbę całkowitą (wpisz <stop> jeżeli chcesz skończyć): "))

while True:
        komenda = (input("Podaj liczbę całkowitą (wpisz [k] jeżeli chcesz skończyć): "))
        if komenda == 'k':
                break
        liczba = int(komenda)
        zbior.add(liczba)

dodatnie = (zbior & doodatnie_do_stu)
print(f"Ilość wszystkich podanych unikatowych liczb: {len(zbior)}")
print(f"Ilość podanych unikatowych liczb dodatnich: {len(dodatnie)}")