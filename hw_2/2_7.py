# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
# равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

number = int(input('Введите число: '))
n = number
formula = n * (n + 1) // 2
summary = 0

while n > 0:
    summary += n
    n -= 1

if formula == summary:
    print(f'Равенство 1+2+...+n = n(n+1)/2 для числа {number} верно. {formula} {summary}')
else:
    print(f'Равенство 1+2+...+n = n(n+1)/2 для числа {number} не верно. {formula} {summary}')

