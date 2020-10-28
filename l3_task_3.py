def my_func():
    x = int(input('Number 1: '))
    y = int(input('Number 2: '))
    z = int(input('Number 2: '))
    list = [x, y, z]
    list.remove(min(list))
    return list[0] + list[1]

print(my_func())