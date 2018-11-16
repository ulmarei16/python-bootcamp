class CashMachine:

    def __init__(self):
        self._available = []  # <--- dodanite podkreslnika powoduje że programisci powinni startac się by ta zmienna byla prywatna, dodanie __ powoduje, że trudniej się do tego dostać, ale to nie jest idealnie
        self.broken = False

    def put_money(self, notes):
        self._available.extend(notes)

    def is_available(self):
        # if self.available != []:
        #     return True
        if self._available:
            return True
        return False

    # def withdraw(self, amount):
    #     bills = []
    #     for bill in sorted(self._available, reverse=True):
    #         if sum(bills) + bill <= amount:
    #             bills.append(bill)
    #             self._available.remove(bill)
    #
    #     if sum(bills) == amount:
    #         for bill in bills:
    #             self._available.remove(bill)
    #         return bills
    #     return []

    def withdraw(self, amount):
        bills_to_whitdraw = []
        for bill in sorted(self._available, reverse=True):
            if sum(bills_to_whitdraw) + bill <= amount:
                bills_to_whitdraw.append(bill)

        if sum(bills_to_whitdraw) == amount:
            for bill in bills_to_whitdraw:
                self._available.remove(bill)
            return bills_to_whitdraw
        return []

# def test_cash_machine_available(): #<--- test passed
#     cash_machine = CashMachine()
#     assert not cash_machine.is_available()

# def test_available_after_put_money(): #<--- test passed
#     cash_machine = CashMachine()
#     cash_machine.put_money([200, 100, 100, 50])
#     assert cash_machine.is_available()

def test_withdraw():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw(150) == [100, 50]
    assert cash_machine.withdraw(150) == []
"""
def test_wrong_amount():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw(90) == []

def test_wrong_order_matter():
    cash_machine = CashMachine()
    cash_machine.put_money([20, 20, 50, 50])
    assert cash_machine.withdraw(100) == [50, 50]

def test_wrong_broken():
    cash_machine = CashMachine()
    assert not cash_machine.broken
"""
# a = [1,2,3]
# b = [4,5]
# a.extend(b) <---- dodaje do siebie listy
# a.sort <--- ustawia pokolei i zmienia listę
# a.sort(reverse=True) <-- ustawia od nawięklszego do najmniejszego i zmienia listę
# sorted(a) <--- tworzy posortowaną kopię listy, nie zmienia listy
