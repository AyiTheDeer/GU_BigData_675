class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')


pen = Pen('Карандаш')
pensil = Pencil('Ручка')
handle = Handle('Маркер')

pen.draw()
pensil.draw()
handle.draw()