import math

print(math.sin(math.pi/2))
print(dir(math))

class Sphere:
    def __init__(self,r):
        self.promien = r

    def objentosc(self):
        return (4/3) * math.pi * math.pow(self.promien,3)

    def pole(self):
        return 4 * math.pi *self.promien ** 2


#tworz klase
# s = Sphere(10)
# s.promien # 10
#
# s.objetosc()
# s.pole()


def test_objetosc():
    objentosc = Sphere(10)
    assert objentosc == 4188.78..

def test_pole():
    pole = Sphere(10)
    assert pole == 1256.63..