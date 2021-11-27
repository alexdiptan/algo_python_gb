# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

number = input('Enter number: ')
# Первый способ
print(number[::-1])

# Второй способ
reverse_number = ''

for digit in list(number)[::-1]:
    reverse_number += digit

print(reverse_number)
