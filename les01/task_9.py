# Задание - 9
# Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).
#
# Блок - схема
# https://drive.google.com/file/d/1NScDQr8tTSD5FFlFVJYLlZbWLlvbraZp/view?usp=sharing

print('Введите три числа:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a > b:
    if c > b:
        if c > a:
            print(f'а = {a} - среднее число')
        else:
            print(f'c = {c} - среднее число')
    else:
        print(f'b = {b} - среднее число')
else:
    if c > a:
        if c > b:
            print(f'b = {b} - среднее число')
        else:
            print(f'c = {c} - среднее число')
    else:
        print(f'а = {a} - среднее число')