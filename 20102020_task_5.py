revenue = int(input('Введите выручку: '))
cost = int(input('Введите издержки: '))

if revenue > cost:
    print('Вы работаете в прибыль')
    print(f'Рентабельность выручки = {revenue / cost:.2f}')
    employees = int(input('Введите количество сотрудников: '))
    print(f'Выручка в расчете на одного отрудника составляет {revenue / employees:.2f}')
elif revenue < cost:
    print('Вы работаете в убыток')
else:
    print('Вы работаете в ноль')