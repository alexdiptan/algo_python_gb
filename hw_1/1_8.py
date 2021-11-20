# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
year = int(input('Enter a year: '))

if year % 400 == 0:
    print(f'{year} високосный 1')
elif year % 100 == 0:
    print(f'{year} не високосный 2')
elif year % 4 == 0:
    print(f'{year} високосный')
else:
    print(f'{year} не високосный')
