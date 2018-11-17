import sys #moduł systemowy

print(sys.path)

#plik __init__.py w katalog to zanczy ten katalog jest python package

#from zadanie_6 import Vector #<-- zaciąga konkretny obiekt z danego modułu

from zjazd_3.zadanie_6 import Vector

v1 = Vector(1,2)
v2 = Vector(1,2)

print(v1+v2)
