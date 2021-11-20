# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он
# разносторонним, равнобедренным или равносторонним.

a = int(input('Enter first triangle side number: '))
b = int(input('Enter second triangle side number: '))
c = int(input('Enter third triangle side number: '))

triangle_sides = [a, b, c]
triangle_sides.sort()

if (triangle_sides[0] + triangle_sides[1]) > triangle_sides[2]:
    print('---This is a triangle---')
    if triangle_sides[0] == triangle_sides[1] == triangle_sides[2]:
        print('Three equal sides triangle.')
    elif triangle_sides[0] == triangle_sides[1] or triangle_sides[0] == triangle_sides[2] or \
            triangle_sides[2] == triangle_sides[1]:
        print('Two equal sides triangle.')
    else:
        print('Different sides triangle.')
else:
    print('There is no triangle here.')
