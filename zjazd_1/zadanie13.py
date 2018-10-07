#napisz program obliczających srednią temperatur podanych przez użytkownika


WEEK = 7
day_no = 1
suma = 0
min_ = None # <-- None przypisuje pustą wartość
max_ = None


while day_no <= WEEK:
    temp = int(input(f"Podaj temperaturę z dnia {day_no}: "))
    suma = suma + temp
    if day_no == 1:
        min_ = temp
        max_ = temp
    else:
        if temp < min_:
            min_ = temp
        if max_ > temp:
            temp = max_

    day_no = day_no + 1



av = suma / day_no
print(f'Średnia temperatur w tygodniu to {av}.')
print(f'minimalna temperatura: {min_}')
print(f'maksymalna temperatura: {max_}')
