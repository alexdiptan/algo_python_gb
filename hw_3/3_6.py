# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint, seed

seed(14)
numb_list = [randint(1, 100) for x in range(10)]
numb_list.sort()
print(numb_list)
total = sum(numb_list[1:-1])

print(f'Максимальный элемент: {numb_list[-1]}, минимальный элемент: {numb_list[0]}, '
      f'сумма элементов между ними: {total}')

