def delenie():
    try:
        arg1 = int(input("Введите число 1: "))
        arg2 = int(input("Введите число 2: "))
        x = arg1 / arg2
    except ZeroDivisionError:
        return 'Деление на 0'
    return x

print(delenie())
