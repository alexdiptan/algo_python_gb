
expression = input('Введите выражение для вычисления: ')
list_expression = expression.split()

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
