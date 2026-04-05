class employee:

    def __init__(self, first, last, annual_salary):
        self.first = first
        self.last = last
        self.annual_salary = annual_salary

    def give_raise(self, money_raise = 5000):
        self.annual_salary += money_raise


