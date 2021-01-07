time = int(input('Введите количество секунд: '))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 360 + minutes * 60)
print(f'Вы ввели {time} секунд. Время в формате  чч:мм:сс {hours}:{minutes}:{seconds}')