#import B


#najpierw powinniśmy importować z bilioteki standardowej
#drugie importujemy rzeczy z biblioteki zewnetrznej
#trzecie importujemy moduły z naszej aplikacji

from B import bar

print("jestem w A")

def foo():
    return "foo z modułu A"

print(foo())
print(bar())