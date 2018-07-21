# Задание - 8.
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать
# ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.
import random

n = 4
print('Заполните матрицу размером 4х4:')
matrix = [[int(input(f'element of matrix = ')) for _ in range(n)] for _ in range(n)]

for line in matrix:
    sum_line = 0
    for el in line:
        sum_line += el
    line.append(sum_line)
    for el in line:
        print(f'\t{el}', end='')
    print()
