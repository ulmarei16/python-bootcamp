class ElectricCar:
    def __init__(self, max_range):
        self.max_range = max_range
        self.left = max_range

    def drive(self, distance):
        if distance >= self.left:
            can_travel = self.left
            self.left = 0
            return can_travel

        self.left -= distance

        return distance

    def charge(self):
        self.left = self.max_range


def test_drive():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30
    assert car.drive(50) == 0
