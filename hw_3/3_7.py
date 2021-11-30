# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны
# между собой (оба являться минимальными), так и различаться.

from random import randint, seed

seed(14)
numb_list = [randint(1, 100) for x in range(10)]
numb_list.sort()
print(numb_list)

print(f'Наименьшие элементы: {numb_list[0]}, {numb_list[1]}.')
