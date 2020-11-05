with open('task6.txt', encoding='utf-8') as file:
    content = file.readlines()
    d = {}
    fin = []
    for i in content:
        i = i.replace('(л)', '')
        i = i.replace('(пр)', '')
        i = i.replace('(лаб)', '')
        i = i.replace('— ', '')
        lst = i.split(': ')

        a = lst[1].split()
        b = sum(list(map(int, a)))
        d[lst[0]] = b
print(d)