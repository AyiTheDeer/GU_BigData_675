from itertools import count, cycle
for i in count(3, 1):
    print(i)
    if i == 10:
        break

my_list = [1, 2, 3]
i = 0
for x in cycle(my_list):
    i += 1
    print(x)
    if i == 30:
        break