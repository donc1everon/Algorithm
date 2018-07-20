# Задание - 3.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

massive = [random.randint(1, 100) for _ in range(10)]
min = 100
max = 0

print(f'Начальный массив - \t\t\t{massive}')

for idx, el in enumerate(massive):
    if min > el:
        min = el
        min_idx = idx
    if max < el:
        max = el
        max_idx = idx

massive[min_idx], massive[max_idx] = massive[max_idx], massive[min_idx]


print(f'Массив после замены мест - \t{massive}')