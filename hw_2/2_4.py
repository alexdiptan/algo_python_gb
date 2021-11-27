# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится
# с клавиатуры.

number = int(input('Введите число. Число должно быть больше 1: '))
element = 1
total = 1

if number > 0:
    while number > 0:
        element /= -2
        total += element
        number -= 1
else:
    print('Введенное число должно быть больше 1')

print(total)
