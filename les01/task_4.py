# Задание - 3
# Написать программу, которая генерирует в указанном
# пользователем диапазоне:
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы
# диапазона. Если надо получить случайный символ от 'a' до 'f',
# вводятся эти символы. Программа должна вывести на экран любой
# символ алфавита от 'a' до 'f' включительно.
#
# Блок - схема
# https://drive.google.com/file/d/1XCeHXRVWjGCsBVBxou9q1J_v8pEI1rSk/view?usp=sharing

import random

print('Введите начало и конец диапозона:')
print('- Целые числа')
print('- Вещественные числа')
print('- Символы')
n = input('n = ')
m = input('m = ')

if n.isdigit() and m.isdigit():
    n = int(n)
    m = int(m)
    rand_num = random.randint(n, m)
    print(f'Случайное число в вашем диапозоне - {rand_num}')
elif n.isalpha() and m.isalpha():
    n = ord(n)
    m = ord(m)
    rand_num = random.randint(n, m)
    rand_sym = chr(rand_num)
    print(f'Случайный символ в вашем диапозоне - {rand_sym}')
else:
    n = float(n)
    m = float(m)
    rand_num = random.uniform(n, m)
    print(f'Случайное число в вашем диапозоне - {rand_num}')
