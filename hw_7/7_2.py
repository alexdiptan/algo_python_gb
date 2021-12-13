# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
from random import randint, seed


def qsort_inplace(lst, start=0, end=None):
    """
    Отсортировать список методом быстрой сортировки
    """
    def subpart(lst, start, end, pivot_point):
        lst[start], lst[pivot_point] = lst[pivot_point], lst[start]
        pivot = lst[start]
        x = start + 1
        y = start + 1

        while y <= end:
            if lst[y] <= pivot:
                lst[y], lst[x] = lst[x], lst[y]
                x += 1
            y += 1

        lst[start], lst[x - 1] = lst[x - 1], lst[start]
        return x - 1

    if end is None:
        end = len(lst) - 1
    if end - start < 1:
        return

    pivot_point = (start + end) // 2
    x = subpart(lst, start, end, pivot_point)
    qsort_inplace(lst, start, x - 1)
    qsort_inplace(lst, x + 1, end)


if __name__ == '__main__':
    seed(13)
    some_list = [round(50 * float(random.random()), 1) for _ in range(20)]
    print(f'Start list: \n {some_list}')
    qsort_inplace(some_list)
    print(f'Sorted list: \n {some_list}')

"""
output: 
Start list: 
 [13.0, 34.3, 34.2, 42.5, 9.3, 11.5, 7.4, 11.3, 36.7, 6.5, 26.6, 10.7, 14.7, 21.6, 41.9, 30.4, 0.7, 13.8, 7.3, 43.6]
Sorted list: 
 [0.7, 6.5, 7.3, 7.4, 9.3, 10.7, 11.3, 11.5, 13.0, 13.8, 14.7, 21.6, 26.6, 30.4, 34.2, 34.3, 36.7, 41.9, 42.5, 43.6]

"""