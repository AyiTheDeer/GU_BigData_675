from sys import argv
hours, hourly_rate, bonus = argv[1:]
print(f'Зарплата сотрудника: {float(hours) * float(hourly_rate) + int(bonus)} шекелей.')