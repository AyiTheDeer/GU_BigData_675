number = abs(int(input('Введите целое положительное число: ')))

big_number = number % 10
#print(big_number)
while number >= 1:
    number = number // 10
    if number % 10 > big_number:
        big_number = number % 10
    if number > 9:
        continue
    else:
        print('Самая большая цифра в числе: ', big_number)
        break