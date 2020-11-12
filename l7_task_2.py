class Clothes:
    def __init__(self, coat_size, costume_height):
        self.coat_size = coat_size
        self.costume_height = costume_height

    @property
    def fabric_coat(self):
        return str(f'Расход ткани на пальто: {(self.coat_size / 6.5 + 0.5):.2f}')

    @property
    def fabric_costume(self):
        return str(f'Расход ткани на костюм: {(self.costume_height * 2 + 0.3):.2f}')

    @property
    def fabric_all(self):
        return str(f'Расход ткани всего: {(self.coat_size / 6.5 + 0.5) + (self.costume_height * 2 + 0.3):.2f}')


order_1 = Clothes(48, 1.74)
print(order_1.fabric_all)
print(order_1.fabric_costume)
print(order_1.fabric_coat)
