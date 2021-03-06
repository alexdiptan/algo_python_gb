# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint, seed

seed(14)
matrix_list = [[0]*5 for i in range(4)]  # создается матрица 5х4 и заполняем её нулями.

# Теперь меняем нули на "случайные числа".
for ind, row in enumerate(matrix_list):
    for elem_ind, elem in enumerate(row):
        matrix_list[ind][elem_ind] = randint(1, 10)

print('\n'.join(map(str, matrix_list)))  # выводим матрицу в красивом виде.
# Само решение. В функцию zip передается матрица. С помощью оператора * (распаковки) получим отдельно списки, для
# которых применится функция zip. Логика в том, что функция zip берет первый элемент из каждого итерируемого
# объекта и формирует из них кортеж. Каждый элемент такого кортежа, будет являться столбцом для исходной матрицы.
# После чего, для каждого такого кортежа, с помощью map, применится функция min, результат этого сформируется список
# минимумов всех столбцов, и в финале, функцией max получим максимальный элемент списка.
print(max(list(map(min, zip(*matrix_list)))))
