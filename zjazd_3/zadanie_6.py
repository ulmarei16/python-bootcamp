#dodawanie __add__(self), odejmowanie, rownosc, mniejsze niz, mnozenie (przez skalar?) __mul__(self)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # new_x = self.x + other.x
        # new_y = self.y + other.y
        # return (new_x, new_y)
        return Vector(self.x+other.x, self.y + other.y)

     def __mul__(self, other):
    #     new_x = self.x * other
    #     new_y = self.y * other
    #     return (new_x, new_y)
        return Vector(self.x * other, self.y * other)


    def __sub__(self, other):
        # new_x = self.x - other.x
        # new_y = self.y - other.y
        # return (new_x, new_y)
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5



def test_dodawanie():
    vect1 = Vector(1,2)
    vect2 = Vector(1,2)
    result = vect1 + vect2

    assert result.x == 2
    assert result.y == 4

def test_mnozenie():
    vect1 = Vector(1, 2)
    assert vect1 * 2 == (2,4)

def test_odejmowanie():
    vect1 = Vector(1, 3)
    vect2 = Vector(4, 7)
    result = vect1 - vect2

    assert result.x == -3
    assert result.y == -4

def test_rowne():
    vect1 = Vector(1, 3)
    vect2 = Vector(1, 3)
    vect3 = Vector(4, 7)

    assert vect1 == vect2
    assert not vect1 == vect3

def test_liczy_dlugosc():
    vect = Vector(2,2)
    assert vect.length() == (2 ** 2 + 2 ** 2) ** 0.5

def test_mniejszy_niz():
    v1 = Vector(1,3)
    v2 = Vector(1,2)

    assert not (v1 < v2)
    assert (v1 > v2)