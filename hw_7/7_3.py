# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
# сложно, то используйте метод сортировки, который не рассматривался на уроках
from random import randint, seed
import statistics


def mediana(dig_array):
    half = len(dig_array) // 2
    dig_array.sort()
    if not len(dig_array) % 2:
        return (dig_array[half - 1] + dig_array[half]) / 2
    return dig_array[half]


if __name__ == '__main__':
    seed(13)
    m = 10
    some_list = [randint(0, 100) for _ in range(2 * m + 1)]
    print(f'Исходный массив: {some_list}')
    print(f'Медиана: {mediana(some_list)}')
    print(f'Медиана из модуля statistics: {statistics.median(some_list)}')

"""
output:
Исходный массив: [33, 37, 87, 87, 23, 83, 29, 85, 18, 28, 82, 93, 23, 16, 9, 68, 27, 95, 37, 3, 55]
Медиана: 37
Медиана из модуля statistics: 37
"""