result = lambda my_func: sum(list(map(int, num)))
answer = 0

while True:
    num = input('Введите числа через пробел или Q для выхода: ').lower().split()
    if 'q' in num:
        answer += result(num.remove('q'))
        print(answer)
        break
    else:
        answer += result(num)
        print(answer)
