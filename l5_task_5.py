with open('task5.txt', 'w+', encoding='utf-8') as file:
    file.write('1 2 3 4 5 6 7 8 9 10 11')
    file.seek(0)
    content = file.read().split()
    num = list(map(int, content))
    print(f'Сумма числе в строке: {sum(num)}')