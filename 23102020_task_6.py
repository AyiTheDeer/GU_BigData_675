base = []
item_id = 0
step = 1

while step !=0:
    name = input('Введите название товара: ')
    price = input('Введите цену товара: ')
    count = input('Введите количество товара: ')
    item_id += 1
    item_description = {'Название:': name, 'Цена': price, 'Количество:': count}
    item = (item_id, item_description)
    base.append(item)
    step = int(input('Хотите ввести еще один товар? 1 = да, 0 = нет: '))

analytics = {}
for i in base:
    for name, price in i[1].items():
        if name in analytics:
            analytics[name].append(price)
        else:
         analytics[name] = [price]
print(analytics)
