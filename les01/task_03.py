# Задание - 3
# По введенным пользователем координатам двух точек вывести
# уравнение прямой, которая проходит через эти точки.
#
# Блок - схема
# https://drive.google.com/file/d/1ost4vTZ3bXHtxcWOW7xns12u7lx_LjQD/view?usp=sharing

print('Введите координаты точки A: ')
x1 = int(input('x1  = '))
y1 = int(input('y1  = '))
print('Введите координаты точки B: ')
x2 = int(input('x2  = '))
y2 = int(input('y2  = '))

A = y1 - y2
B = x2 - x1
C = x1*y2 - x2*y1

print(f'Уравнение прямой - {A}*x + {B}*y + {C} = 0')