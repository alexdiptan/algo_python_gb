# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более
# чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

from random import randint

number = randint(0, 100)
assume = int(input('Введите число: '))
attempt_count = 10
attempt = 0

while assume != number:
    if attempt == attempt_count:
        print(f'Попытки закончились. Вы не угадали. Загаданное число = {number}')
        break
    elif assume < number:
        print(f'Ваше число меньше загаданного.')
    elif assume > number:
        print(f'Ваше число больше загаданного.')
    elif assume == number:
        print(f'Вы выиграли! Кол-во попыток = {attempt}\nзагаданное число = {number}\n')
        break
    else:
        print('Что то пошло не так.')

    attempt += 1
    assume = int(input(f'Попытка: {attempt}. Введите число: '))

