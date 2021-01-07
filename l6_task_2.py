class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.Qmetr_Weight = 25
        self.sm = 5

    def weight(self):
        return print(f'Масса асфальта: {self._length * self._width * self.Qmetr_Weight * self.sm / 1000:.2f}т.')

road = Road(20, 5000)
road.weight()