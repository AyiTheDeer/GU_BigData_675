with open('task2.txt', encoding='utf-8') as file:
    n_lines = len(file.readlines())
    print(f'Количество строк в файле: {n_lines}')
    file.seek(0)
    line = 0
    for i in file.readlines():
        words = len(i.split())
        line += 1
        print(f'Количество слов в строке {line}: {words}')