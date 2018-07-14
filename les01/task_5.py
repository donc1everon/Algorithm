# Задание - 5
# Пользователь вводит две буквы. Определить их порядковый номер в алфавите и рассчитать
# число букв между ними
#
# Блок - схема
# https://drive.google.com/file/d/1WKuX2a21SeLX8hGT92bw1aX-x1KTKodF/view?usp=sharing

import random

print('Введите 2 буквы:')
n = input('Первая буква: ')
m = input('Вторая буква: ')

num_n = ord(n) - ord('a') + 1
num_m = ord(m) - ord('a') + 1
num_between = abs(num_n - num_m - 1)

print(f'Порядковый номер первой буквы - {num_n}')
print(f'Порядковый номер второй буквы - {num_m}')
print(f'Расстояние между первой и второй буквой - {num_between}')