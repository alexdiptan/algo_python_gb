# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint, seed

seed(14)

numb_list = [randint(1, 100) for x in range(10)]
print(numb_list)
min_number = min(numb_list)
max_number = max(numb_list)

print(max_number, min_number)

for index, item in enumerate(numb_list):
    if item == min_number:
        numb_list[index] = max_number
    elif item == max_number:
        numb_list[index] = min_number
print(numb_list)
