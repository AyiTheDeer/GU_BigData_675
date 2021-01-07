n_month = int(input('Введите номер месяца от 1 до 12: '))

li = ['winter', 'spring', 'summer', 'fall']
di = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'fall'}
if n_month == 1 or n_month == 2 or n_month == 12:
    print(f'Список говорит, что это {li[0]}. И словарь говорит, что это {di.get(1)}')
elif n_month == 3 or n_month == 4 or n_month == 5:
    print(f'Список говорит, что это {li[1]}. И словарь говорит, что это {di.get(2)}')
elif n_month == 6 or n_month == 7 or n_month == 8:
    print(f'Список говорит, что это {li[2]}. И словарь говорит, что это {di.get(3)}')
elif n_month == 9 or n_month == 10 or n_month == 11:
    print(f'Список говорит, что это {li[3]}. И словарь говорит, что это {di.get(4)}')
else:
    print('Такого месяца нет')
