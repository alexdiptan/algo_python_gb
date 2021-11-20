from random import randrange, uniform, choice

print('---Целые числа---')
int_x = int(input('Введите левую границу диапазона чисел: '))
int_y = int(input('Введите правую границу диапазона чисел: '))

if int_x < int_y:
    print(randrange(int_x, int_y))
else:
    print('Правая граница диапазона меньше левой.')

print('---Вещественные числа---')
float_x = float(input('Введите левую границу диапазона чисел: '))
float_y = float(input('Введите правую границу диапазона чисел: '))

if float_x < float_y:
    print(uniform(float_x, float_y))
else:
    print('Правая граница диапазона меньше левой.')

print("---Случайная буква---")
first_letter = input('Введите левую границу диапазона букв: ')
second_letter = input('Введите правую границу диапазона букв: ')

alpha_list = []

if ord(first_letter) < ord(second_letter):
    for rand_symb in range(ord(first_letter), ord(second_letter)):
        alpha_list.append(chr(rand_symb))

    print(choice(alpha_list))
else:
    print('Вы ввели не корректный диапазон букв.')

