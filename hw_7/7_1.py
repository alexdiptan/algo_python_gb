# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint, seed

seed(13)
# dig_list = [randint(-100, 100) for x in range(10)]
dig_list = [8, 7, 1, 5]

print(dig_list)
for ind, dig in enumerate(dig_list):
    if ind < len(dig_list):
        if dig_list[ind] > dig_list[ind-1]:
            print(dig_list[ind], dig_list[ind-1])
            dig_list[ind], dig_list[ind - 1] = dig_list[ind - 1], dig_list[ind]


print(dig_list)
