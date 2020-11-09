class Car:
    def __init__(self):
        self.speed = 0
        self.color = None
        self.name = None
        self.is_police = False

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn_left(self):
        print(f'{self.name} повернула налево')

    def turn_right(self):
        print(f'{self.name} повернула направо')

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} Скорость превышена')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} Скорость превышена')

moskvich = Car()
moskvich.name = 'moskvich'
moskvich.speed = 100
moskvich.color = 'white'
moskvich.is_police = False

moskvich.go()
moskvich.turn_left()
moskvich.stop()
print(moskvich.show_speed())

moskvich2 = TownCar()
moskvich2.name = 'moskvich2'
moskvich2.speed = 100
moskvich2.color = 'white'
moskvich2.is_police = False

moskvich2.show_speed()