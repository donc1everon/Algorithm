# Задание - 6
# Пользователь вводит номер буквы в алфавите. Определить, какая это буква
#
# Блок - схема
# https://drive.google.com/file/d/1vvqjt9H-mc9QOCXyvNIImbWdMS_9D7la/view?usp=sharing

import random

print('Введите номер буквы:')
num = input('Номер буквы: ')

letter = chr(int(num) + ord('a') - 1)

print(f'Ваша буква - {letter}')