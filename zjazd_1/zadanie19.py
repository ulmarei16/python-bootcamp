li = []

for x in range(0, 101):
    if x % 3 == 0 or x % 5 == 0:
        li.append(x)

print("Liczby podzielne przez 3 lub 5: ")
for el in li:
    print(el)

print("") #dodaje wiersz odstępu
print("W tym przedziale jest ", len(li), " takich liczb.")


# można też: li = list(range(101)