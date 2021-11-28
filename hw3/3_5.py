# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint, seed

seed(14)

negative_numbers = [randint(-50, 0) for x in range(15)]
print(negative_numbers)

max_negative_number = min(negative_numbers)
max_negative_numbers_index = 0

for ind, item in enumerate(negative_numbers):
    if item > max_negative_number:
        max_negative_number = item
        max_negative_numbers_index = ind

print(f'Максимальное отрицательное число: {max_negative_number}, индекс числа: {max_negative_numbers_index}')
