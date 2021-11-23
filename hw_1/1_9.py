# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
digit_one = int(input('Enter the first number: '))
digit_two = int(input('Enter the second number: '))
digit_three = int(input('Enter the third number: '))

digit_list = [digit_three, digit_two, digit_one]
digit_list.sort()
print(f'List is {digit_list}. Middle digit is {digit_list[1]}')
