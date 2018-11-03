#Stworz klase Dog wg nastepujacej specyfikacj
# pies zuzywa energie szczekajac

class Dog:
    def __init__(self):
        self.energy = 10

    def bark(self):
        self.energy -= 1

    def sleep(self):
        self.energy += 2

    def get_energy(self):
        return self.energy

azor = Dog()

def test_azor():
     assert azor.get_energy() == 10


# azor.sleep()
# print(azor.get_energy())