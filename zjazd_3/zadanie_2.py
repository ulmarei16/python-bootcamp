class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.time = 0


    def register_time(self, time):
        self.time += time

    def pay_salary(self):
        if self.time <= 8:
            pay = self.time * self.salary
        elif self.time > 8:
            pay = 8 * self.salary + (self.time - 8) * self.salary * 2
        self.time = 0
        return pay

class PremiumEmployee(Employee):
    def __init__(self, name, surname, salary):
        #Employee.__init__(self, name, surname, salary)
        super().__init__(name,surname,salary)
        self.bonus = 0

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        pay_bonus = super().pay_salary()
        return pay_bonus + self.bonus


class Company:
    def __init__(self, name):
        self.name = name
        self.payroll = set()


    def add_employee(self, employee):
        self.payroll.add(employee)

    def total_staff(self):
        return len(self.payroll)

    def pay_all_salary(self):
        sum_ = 0

        for e in self.payroll:
           sum_ += e.pay_salary()

        return sum_


def test_employee():
    employee = Employee("Jan", "Nowak", 100)
    assert employee.name == "Jan"
    assert employee.surname == "Nowak"
    assert employee.salary == 100

def test_pay_salary():
    employee = Employee("Jan", "Nowak", 100)
    employee.register_time(5)
    assert employee.pay_salary() == 500

def test_pay_no_second_salary():
    employee = Employee("Jan", "Nowak", 100)
    employee.register_time(5)
    assert employee.pay_salary() == 500
    assert employee.pay_salary() == 0

def test_pay_salary_overtime():
    employee = Employee("Jan", "Nowak", 100)
    employee.register_time(10)
    assert employee.pay_salary() == 1200

def test_premium():
    employee = PremiumEmployee("Jan", "Nowak", 100)
    employee.register_time(5)
    employee.give_bonus(1000)
    assert employee.pay_salary() == 1500

def test_company():
    employee = Employee("Jan", "Nowak", 100)
    employee.register_time(5)
    google = Company("google")
    google.add_employee(employee)
    assert google.total_staff() == 1
    assert google.pay_all_salary() == 500
    assert google.pay_all_salary() == 0
    employee2 = Employee("Krzysztof", "Nowak", 200)
    employee2.register_time(5)
    employee.register_time(10)
    google.add_employee(employee2)
    assert google.pay_all_salary() == 2200

# utworz klase company, ktora inicuje sie z nazwa
# employee = Employee("Jan", "Nowak", 100)
# employee.register_time(5)
# google = Company("google")
# google.add_employee(employee)
# google.size()
# 1
# google.pay_all_salary()
# 500
# google.pay_all_salary()
# 0 <--- zeruje bo juz wyplacil
# employee2 = Employee("Krzysztof", "Nowak", 100)
# employee.register_time(5)
# google.add_employee(employee2)