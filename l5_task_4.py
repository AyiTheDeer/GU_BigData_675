with open('task4.txt', encoding='utf-8') as file:
    content = file.readlines()
    new = []
    for i in content:
        i = i.split(' — ')
        if i[0] == 'One':
            i[0] = 'Один'
            new.append(i[0] + ' - ' + i[1])
        if i[0] == 'Two':
            i[0] = 'Два'
            new.append(i[0] + ' - ' + i[1])
        if i[0] == 'Three':
            i[0] = 'Три'
            new.append(i[0] + ' - ' + i[1])
        if i[0] == 'Four':
            i[0] = 'Четыре'
            new.append(i[0] + ' - ' + i[1])

with open('task4_new.txt', 'w', encoding='utf-8') as file_2:
    file_2.writelines(new)