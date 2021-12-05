# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить
# их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

list_first_number = list(input('Введите первое число в шестнадцатиричном формате: '))  # 'A2'
list_second_number = list(input('Введите второе число в шестнадцатиричном формате: '))  # 'C4F'


def from_list_to_str(number):
    return ''.join(number)


def addition_numbers_dec(num_one, num_two):
    result = int(num_one, 16) + int(num_two, 16)
    print(f'Десятичное представление чисел: {(int(num_one, 16))} + {int(num_two, 16)} = {result}')
    return result


def mult_numbers_dec(num_one, num_two):
    result = int(num_one, 16) * int(num_two, 16)
    print(f'Десятичное представление чисел: {(int(num_one, 16))} * {int(num_two, 16)} = {result}')
    return result


first_number, second_number = from_list_to_str(list_first_number), from_list_to_str(list_second_number)

print(f'Результат операции сложение: {first_number} + {second_number} = '
      f'{hex(addition_numbers_dec(first_number, second_number)).upper()[2:]}')

print(f'Результат операции умножение: {first_number} * {second_number} = '
      f'{hex(mult_numbers_dec(first_number, second_number)).upper()[2:]}')

"""

output:
Введите первое число в шестнадцатиричном формате: 5A3
Введите второе число в шестнадцатиричном формате: A2
Десятичное представление чисел: 1443 + 162 = 1605
Результат операции сложение: 5A3 + A2 = 645
Десятичное представление чисел: 1443 * 162 = 233766
Результат операции умножение: 5A3 * A2 = 39126

"""
