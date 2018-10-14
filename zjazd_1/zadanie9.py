import datetime

now = datetime.datetime.now()

print(now.year)
print(now.month)

wiek = int(input("Podaj rok urodzenia: "))

pelnoletni = now.year - wiek

if pelnoletni > 18:
    print("Jesteś pełnoletni/pełnoletnia!")
else:
    print("Zjeżdzaj smarkaczu!")