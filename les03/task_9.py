# Задание - 9.
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

n = 4
matrix = [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]
min_column = [100] * len(matrix)

for line in matrix:
    for idx, el in enumerate(line):
        print(f'\t{el}', end='')
        if el < min_column[idx]:
            min_column[idx] = el
    print()

print(f'Максимальный элемент среди минимальных в столбце = {max(min_column)}')
