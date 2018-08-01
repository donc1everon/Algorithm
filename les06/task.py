import platform
import sys
import random

print('*' * 50)
arh = list(platform.architecture())
print(f'Версия Python - {platform.python_version()}\nРазрядность системы - {arh[0]}')
print('*' * 50)

count = 1

def research_memory(*args):
    global count
    print(f'Исследование №{count}')
    count += 1
    for arg in args:
        return sys.getsizeof(arg)


# task - 1
lst_of_chr = []
ord = 32
string = ''
n_pair = 0

for i in range(32, 128):
    lst_of_chr.append(chr(i))

for sym in lst_of_chr:
    string = string + str(ord) + ' - ' + sym + '  |  '
    n_pair += 1
    ord += 1
    if n_pair == 10:
        # print(string)
        string = ''
        n_pair = 0
# print(string)

print(f'Переменная list - {research_memory(lst_of_chr)}')

# task - 2
# Та же самая задача, но создаем сразу под заранее известное количество
# Экономя тем самым почти десятую часть
lst_of_chr = [None] * (128 - 32)
ord = 32
string = ''
n_pair = 0

for idx, i in enumerate(range(32, 128)):
    lst_of_chr[idx] = chr(i)

for sym in lst_of_chr:
    string = string + str(ord) + ' - ' + sym + '  |  '
    n_pair += 1
    ord += 1
    if n_pair == 10:
        # print(string)
        string = ''
        n_pair = 0
# print(string)

print(f'Переменная list, с заранее известным размеров - {research_memory(lst_of_chr)}')

# task - 3
num = '1234567'
even = 0

for i in num:
    i = int(i)
    if i % 2 == 0:
        even += 1

print(f'Переменная even (обычное число класс int) - {research_memory(even)}')

# task - 4
zero = 0    # Даже нулевая матрица весит большую часть
n = 4   # 1 - 4 включительно имеют один размер
m = 8  # 5 - 8 включительно имеют один размер
matrix_0 = [[random.randint(0, 100) for _ in range(zero)] for _ in range(zero)]
matrix = [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]
matrix_2 = [[random.randint(0, 100) for _ in range(m)] for _ in range(m)]

min_column = [100] * len(matrix)

# for line in matrix_0:
#     for idx, el in enumerate(line):
#         print(f'\t{el}', end='')
#         if el < min_column[idx]:
#             min_column[idx] = el
#     print()

print(f'Матрица размером 0 занимает места: {research_memory(matrix_0)}')
print(f'Матрица размерами 1 - 4 занимает места: {research_memory(matrix)}')
print(f'Матрица размерами 5 - 8 занимает места: {research_memory(matrix_2)}')
