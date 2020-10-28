#Var 1
def my_func(x, y):
    return x ** y
print(my_func(2, -3))

#Var 2
def my_func(x, y):
    if y < 0:
        return 1 / x ** abs(y)
    if y > 0:
        return x ** y
    if y == 0:
        return 1

print(my_func(2, -3))
