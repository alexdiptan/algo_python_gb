# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
x_one = int(input('Введите x1: '))
y_one = int(input('Введите y1: '))
x_two = int(input('Введите x2: '))
y_two = int(input('Введите y2: '))

k = (y_one - y_two) / (x_one - x_two)
b = y_one - (k * x_one)

print(f'y = {k} * x + {b} ')
