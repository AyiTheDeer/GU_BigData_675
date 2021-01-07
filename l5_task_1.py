with open('task1.txt', 'w', encoding='utf8') as file:
    while True:
        txt = input('Введите текст: ')
        file.write(txt + '\n')
        if not txt:
            break
file = open('task1.txt', encoding='utf-8')
content = file.readlines()
print(content)
