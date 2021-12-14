# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import cProfile
from random import randint, seed

seed(13)


def bubbles_sort(dig_list):
    for j in range(len(dig_list)-1):
        swap = True
        for i in range(len(dig_list) - j - 1):
            if dig_list[i] > dig_list[i+1]:
                dig_list[i], dig_list[i+1] = dig_list[i+1], dig_list[i]
                swap = False
        if swap:
            break
    return dig_list


if __name__ == '__main__':
    some_list = [randint(-100, 100) for x in range(30)]
    print(f'Start list: \n {some_list}')
    print(f'Sorted list: \n {bubbles_sort(some_list)}')
    # cProfile.run('bubbles_sort(some_list)')


"""
Output:
Start list: 
 [-34, -26, 75, 75, -53, 66, -41, 70, -63, -43, 64, 87, -53, -67, -82, 36, -46, 90, -25, -93, 10, -68, 75, 55, -97, -30, -63, -79, -33, 15]
Sorted list: 
 [-97, -93, -82, -79, -68, -67, -63, -63, -53, -53, -46, -43, -41, -34, -33, -30, -26, -25, 10, 15, 36, 55, 64, 66, 70, 75, 75, 75, 87, 90]


Если за во внутреннем цикле, не сделали ни одной перестановки, значит, список отсортирован и можно завершать работу
функции. Получается, что не обязательно бегать до конца все элементы и мы экономим время. Если проверить
с помощью cProfile на 300 элементах списка, видно, что он бегает 277 раз, а это ускорение работы ~ 10%.

         277 function calls in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.006    0.006    0.006    0.006 7_1.py:11(bubbles_sort)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
      273    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""
