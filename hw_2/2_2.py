# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у
# него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

n = input('Введите натуральное число: ')
even_digit = 0
not_even_digit = 0

for digit in list(n):
    if int(digit) % 2 == 0:
        even_digit += 1
    else:
        not_even_digit += 1

print(f'В числе {n} {even_digit} чётных цифр и {not_even_digit} не чётных.')