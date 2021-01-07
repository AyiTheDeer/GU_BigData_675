li = []
i = 1
while i != 0:
    li.append(input('Введите новое значение списка: '))
    i = int(input('Хотите добавить еще один элемент в список? 1 = да, 0 = нет: '))

x = 0
for a in range(int(len(li)/2)):
    li[x], li[x + 1] = li[x + 1], li[x]
    x += 2
print(li)
