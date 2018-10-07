li = [-1, 100, 20, 30, -15, 0, 200, -100]
dodatnie = 0
ujemne = 0
dodatnieli = []
ujemneli = []

for liczba in li:
    if liczba > 0:
        dodatnie = dodatnie + 1
        dodatnieli.append(liczba)
    if liczba < 0:
        ujemne = ujemne + 1
        ujemneli.append(liczba)

print("ilość liczb dodatnich: ", dodatnie)
print("ilość liczb ujemnych: ", ujemne)
print("ilość liczb dodatnich: ", len(dodatnieli))
print("ilość liczb ujemnych: ", len(ujemneli))