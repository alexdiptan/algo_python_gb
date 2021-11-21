# first_number = int(input('Введите первое число: '))
# second_number = int(input('Введите второе число: '))
# sign = input('Введите тип операции над числами (0, +, -, *, /): ')

expression = '5 + 2'  # input('Введите выражение для вычисления: ')
list_expression = list(expression)

while list_expression[1] != 0:
    expression = input('Введите выражение для вычисления: ')
    list_expression = expression.split()
    print(list_expression)
    if list_expression[1] == '0':
        print('Знак операции 0. Выходим из программы.')
        break
    else:
        print(eval(expression))

print('Программа завершена.')
