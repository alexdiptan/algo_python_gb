# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

numb_range_big = [item for item in range(2, 99)]
numb_range_small = [item for item in range(2, 9)]

for number_small in numb_range_small:
    numbers_count = 0
    for number_big in numb_range_big:
        if number_big % number_small == 0:
            numbers_count += 1
    print(f'Число {number_small} - кратно для {numbers_count} чисел из большого списка.')

print('--------------------------------------------------------')
# или второй вариант решения:
for number_small in numb_range_small:
    print(f'Число {number_small} - кратно для {len([x for x in numb_range_big if x % number_small == 0])} '
          f'чисел из большого списка.')
