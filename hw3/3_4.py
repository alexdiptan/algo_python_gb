# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint, seed

seed(14)
numb_list = [randint(1, 100) for x in range(80)]
print(numb_list)

max_count = 0
number = 0

for x in numb_list:
    if max_count < numb_list.count(x):
        max_count = numb_list.count(x)
        number = x

print(f'Максимум вхождений ({max_count}) найдено для числа {number}.')
