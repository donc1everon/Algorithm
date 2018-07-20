# Задание - 6.
# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
import random

n = 10
massive = [random.randint(1, 100) for _ in range(n)]
min = 100
max = 0

print(f'Массив - \t\t\t{massive}')

for idx, el in enumerate(massive):
    if min > el:
        min = el
        min_idx = idx
    if max < el:
        max = el
        max_idx = idx

if min_idx < max_idx:
    summ = sum(massive[(min_idx + 1):max_idx])
else:
    summ = sum(massive[(max_idx + 1):min_idx])

print(summ)