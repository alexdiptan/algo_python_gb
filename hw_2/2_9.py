# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это
# число и сумму его цифр.
numbers = input('Введите числа разделенные пробелом: ')

list_numbers = numbers.split()
max_digit_summ = 0
max_number = 0

for number in list_numbers:
    list_digits = [int(digit) for digit in number]
    digit_summ = sum(list_digits)
    if digit_summ > max_digit_summ:
        max_digit_summ = digit_summ
        max_number = number

print(f'Число - {max_number} сумма цифр - {max_digit_summ}')
