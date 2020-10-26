my_str = input('Введите строку: ')
li = my_str.split(' ')
num = 0

for word in li:
    if len(word) > 10:
        num += 1
        print(f'{num}. {word[:10]}')
    else:
        num += 1
        print(f'{num}. {word}')