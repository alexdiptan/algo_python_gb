# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых
# трех уроков. Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# В качестве примера, взял пример из задания 3_8
from random import randint, seed

seed(14)
matrix_list = [[0]*5 for i in range(4)]

for ind, row in enumerate(matrix_list):
    for elem_ind, elem in enumerate(row):
        if elem_ind < 4:
            matrix_list[ind][elem_ind] = randint(1, 10)
        elif elem_ind == 4:
            matrix_list[ind][elem_ind] = sum(row)
    print(row)

