class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


worker = Position('Иван', 'Иванов', 'Маркетолог', 1000, 1000)
print(worker.get_full_name())
print(worker.get_total_income())
