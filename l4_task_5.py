from functools import reduce
def my_f(x, y):
    return x * y

my_list = list(range(100, 1001, 2))
print(f'Результат перемножения элементов: {reduce(my_f, my_list)}')
