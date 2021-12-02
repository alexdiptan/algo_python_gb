# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых
# трех уроков. Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# В качестве примера, взял задание 3_8
import cProfile
from random import randint, seed

seed(12)


def get_random_digit(from_digit=1, to_digit=9999):
    return randint(from_digit, to_digit)


def get_matrix(lines_count=5, column_count=4):
    matrix_list = [[0] * lines_count for _ in range(column_count)]
    return matrix_list


def matrix_calculate(matrix_list, multiplier=1):
    for ind, row in enumerate(matrix_list):
        for elem_ind, elem in enumerate(row):
            if elem_ind < len(row) - 1:
                row[elem_ind] = get_random_digit() ** multiplier
            elif elem_ind == len(row) - 1:
                matrix_list[ind][elem_ind] = sum(row)

    return matrix_list


def get_matrix_improved(multiplier=1, lines_count=5, column_count=4):
    matrix_list = [[get_random_digit() ** multiplier for _ in range(lines_count)] for _ in range(column_count)]
    return matrix_list


def matrix_calculate_improved(matrix_list):
    for ind, row in enumerate(matrix_list):
        row[len(row) - 1] = 0
        row[len(row) - 1] = sum(row)

    return matrix_list


def start_matrix_calc():
    matrix = get_matrix(5, 4)
    return matrix_calculate(matrix, 19999)


def start_matrix_calc_improved():
    matrix_improved = get_matrix_improved(19999, 5, 4)
    return matrix_calculate_improved(matrix_improved)


if __name__ == '__main__':
    # cProfile.run('start_matrix_calc()')
    cProfile.run('start_matrix_calc_improved()')

"""
Сделал 2 реализации функции которая суммирует ячейки матрицы - matrix_calculate и matrix_calculate_improved. Разница
между этими функциями в том, что заполнение матрицы значениями происходит по разному. В случае с matrix_calculate
матрица формируется функцией get_matrix, но значения ячеек матрицы равны 0. По этому, в matrix_calculate сделано
2 цикла, один идет по ячейкам матрицы, а второй идет по значениям ячейки матрицы и меняет 0 на рандомное число 
возведенное в степень. 
В случае же с matrix_calculate_improved, она сумирует матрицы, которые подаются на вход. Формирование матрицы, 
заполнение значений ячеек матрицы и возведение числа в степень, делается функцией get_matrix_improved. 

В качестве вывода.
В случае маленьких данных, функции работаю одинаково быстро. Но если увеличить сложность вычислений - функция 
matrix_calculate работает немного быстрее. На мой взгял, такое поведение
обусловлено "накладными расходами". В случае matrix_calculate, вычисления происходят немного быстрее, 
за счет того что заполнение ячеек матрицы происходит шаг за шагом в той же функции. 
В случае же matrix_calculate_improved, сначала матрица формируется функцией get_matrix_improved, если вычисления
сложные, то формируется большой массив данных. Обращение к такому массиву данных происходит дольше, на это тратится
больше процессорного времени.
 
Ниже пример вычислений. Для наглядности измерений, я добавил 2 дополнительные функции start_matrix_calc и 
start_matrix_calc_improved. Они возвращают результат работы функций get_matrix, matrix_calculate и get_matrix_improved,
matrix_calculate_improved. 
В измерениях формируются одни и те же значения - матрица 5х4 заполняется рандомными числами от 1 до 9999. Меняется
только степень, в которую возводится число.


Для начала запускаю start_matrix_calc, числа ячеек матрицы возводится в степень 9999.

         140 function calls in 0.019 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       16    0.000    0.000    0.000    0.000 4_1.py:11(get_random_digit)
        1    0.000    0.000    0.000    0.000 4_1.py:15(get_matrix)
        1    0.000    0.000    0.000    0.000 4_1.py:16(<listcomp>)
        1    0.019    0.019    0.019    0.019 4_1.py:20(matrix_calculate)
        1    0.000    0.000    0.019    0.019 4_1.py:44(start_matrix_calc)
        1    0.000    0.000    0.019    0.019 <string>:1(<module>)
       16    0.000    0.000    0.000    0.000 random.py:238(_randbelow_with_getrandbits)
       16    0.000    0.000    0.000    0.000 random.py:291(randrange)
       16    0.000    0.000    0.000    0.000 random.py:335(randint)
        1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
       24    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
       16    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       25    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


Теперь запускаю start_matrix_calc_improved. Числа ячеек матрицы возводится в степень 9999.


         149 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       20    0.000    0.000    0.000    0.000 4_1.py:11(get_random_digit)
        1    0.000    0.000    0.023    0.023 4_1.py:31(get_matrix_improved)
        1    0.000    0.000    0.023    0.023 4_1.py:32(<listcomp>)
        1    0.000    0.000    0.000    0.000 4_1.py:36(matrix_calculate_improved)
        1    0.000    0.000    0.023    0.023 4_1.py:49(start_matrix_calc_improved)
        1    0.000    0.000    0.023    0.023 <string>:1(<module>)
       20    0.000    0.000    0.000    0.000 random.py:238(_randbelow_with_getrandbits)
       20    0.000    0.000    0.000    0.000 random.py:291(randrange)
       20    0.000    0.000    0.000    0.000 random.py:335(randint)
        1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
       20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       30    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


Запускаю start_matrix_calc. Числа ячеек матрицы возводится в степень 19999.


        140 function calls in 0.055 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       16    0.000    0.000    0.000    0.000 4_1.py:11(get_random_digit)
        1    0.000    0.000    0.000    0.000 4_1.py:15(get_matrix)
        1    0.000    0.000    0.000    0.000 4_1.py:16(<listcomp>)
        1    0.055    0.055    0.055    0.055 4_1.py:20(matrix_calculate)
        1    0.000    0.000    0.055    0.055 4_1.py:44(start_matrix_calc)
        1    0.000    0.000    0.055    0.055 <string>:1(<module>)
       16    0.000    0.000    0.000    0.000 random.py:238(_randbelow_with_getrandbits)
       16    0.000    0.000    0.000    0.000 random.py:291(randrange)
       16    0.000    0.000    0.000    0.000 random.py:335(randint)
        1    0.000    0.000    0.055    0.055 {built-in method builtins.exec}
       24    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
       16    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       25    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


Запускаю start_matrix_calc_improved. Числа ячеек матрицы возводится в степень 19999.


     149 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       20    0.000    0.000    0.000    0.000 4_1.py:11(get_random_digit)
        1    0.000    0.000    0.067    0.067 4_1.py:31(get_matrix_improved)
        1    0.000    0.000    0.067    0.067 4_1.py:32(<listcomp>)
        1    0.000    0.000    0.000    0.000 4_1.py:36(matrix_calculate_improved)
        1    0.000    0.000    0.067    0.067 4_1.py:49(start_matrix_calc_improved)
        1    0.000    0.000    0.067    0.067 <string>:1(<module>)
       20    0.000    0.000    0.000    0.000 random.py:238(_randbelow_with_getrandbits)
       20    0.000    0.000    0.000    0.000 random.py:291(randrange)
       20    0.000    0.000    0.000    0.000 random.py:335(randint)
        1    0.000    0.000    0.067    0.067 {built-in method builtins.exec}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
       20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       30    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

"""
