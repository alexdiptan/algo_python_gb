# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
digit_one = 754
digit_two = 193
digit_three = 337

digit_list = [digit_three, digit_two, digit_one]
digit_list.sort()
print(f'List is {digit_list}. Middle digit is {digit_list[1]}')
