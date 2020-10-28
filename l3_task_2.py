def my_func():
    first_name = input('Enter name: ')
    second_name = input('Enter second name: ')
    year = int(input('Enter year: '))
    city = input('Enter City: ')
    email = input('Enter email: ')
    phone = input('Enter phone: ')
    return f'Name - {first_name}, Surname - {second_name}, Birthday - {year}, City - {city}, Email - {email}, phone - {phone}'

print(my_func())
