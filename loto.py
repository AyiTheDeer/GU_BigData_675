import random


class Card:
    __crossednum = -1
    __emptynum = 0

    def __init__(self):
        self.__ticket = []

        __ticket_numbers = [random.choice(list(range(1, 91))) for x in range(15)]
        __my_list = [__ticket_numbers[i:i + 5] for i in range(0, len(__ticket_numbers), 5)]
        for line in __my_list:
            line.sort()
            k = 0
            while k < 4:
                line.insert(random.randint(0, 4), ' ')
                k += 1
            self.__ticket.append(line)

    def __str__(self):
        border = '-' * 26
        result = border + '\n'
        for i in self.__ticket:
            result += ' '.join(map(str, i)) + '\n'
        return f'{result}'


class Game:
    def __init__(self):
        self.human = Card()
        self.computer = Card()
        self.keg_bucket = list(range(1, 91))

    def game(self):
        keg = self.keg_bucket.pop(random.randint(1, 90))
        print(f'Игрок: \n {self.human}')
        print(f'Компьютер: \n {self.computer}')
        print(f'Число: {keg} Осталось: {len(self.keg_bucket)}')
        answer = input('Зачеркнуть цифру? (y/n)').lower().strip()



player_1 = Card()
player_2 = Card()

# print(player_1.random_ticket())
# print(player_2)
game = Game()
game.game()
