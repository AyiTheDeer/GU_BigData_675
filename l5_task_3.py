with open('task3.txt', encoding='utf-8') as file:
    d = {}
    for line in file:
        (key, val) = line.split()
        d[key] = int(val)

names = []
for name, salary in d.items():
    if salary < 20000:
        names.append(name)
print('Зарплата ниже 20К у:', ', '.join(names))
print(f'Средняя зарплата: {int(sum(d.values()) / len(d))} шекелей')

