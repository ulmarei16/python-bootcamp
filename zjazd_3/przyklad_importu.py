#plik z rozszerzeniem .py to tak zwany moduł
#można w pychamr zrobić mark directory as source root i pycharm bedzie wiedzial gdzie szukac plikow

"""sposób 1."""
import zadanie_6 #<---zaciąga cały taki moduł

v1 = zadanie_6.Vector(1,2)
v2 = zadanie_6.Vector(1,2)

print(v1+v2)

"""sposób 2"""

from zadanie_6 import Vector #<-- zaciąga konkretny obiekt z danego modułu
v1 = Vector(1,2)
v2 = Vector(1,2)

print(v1+v2)

#from zadanie_6 import sth as cos_inneg #<-- dodaje alias jakiemiuś obiektowi z modulu, żeby nie nadpisać nazw innych rzeczy

#zbiór modułów to package a to jest po prostu katalog pytona