import json
profit = {}
avg_profit = {}
a = 0
average = 0
i = 0
with open('task7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            a = a + profit.setdefault(name)
            i += 1
        average = a / i
    print(f'Average profit - {average:.2f}')

    avg_profit = {'Average profit': round(average)}
    profit.update(avg_profit)
    print(f'Profit - {profit}')

with open('task7.json', 'w') as js:
    json.dump(profit, js)