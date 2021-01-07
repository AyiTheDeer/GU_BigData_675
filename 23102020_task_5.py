my_list = [7, 5, 3, 3, 2]
new_number = 1

while new_number != 0:
    new_number = int(input('Введите новое число рейтинга или 0 для отмены: '))
    my_list.append(new_number)
    my_list.sort(reverse=True)
    print(my_list)
