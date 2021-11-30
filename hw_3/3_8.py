# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

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
