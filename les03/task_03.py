# Задание - 3.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

massive = [random.randint(1, 100) for _ in range(10)]
min_el= 100
max_el= 0

print(f'Начальный массив - \t\t\t{massive}')

for idx, el in enumerate(massive):
    if min_el> el:
        min_el= el
        min_idx = idx
    if max_el< el:
        max_el= el
        max_idx = idx

massive[min_idx], massive[max_idx] = massive[max_idx], massive[min_idx]

print(f'Массив после замены мест - \t{massive}')

# вариант 2
i_min = massive.index(min(massive))
i_max = massive.index(max(massive))

spam = massive[i_min]
massive[i_min] = massive[i_max]
massive[i_max] = spam

print(f'Замена мест при \nпомощи встроенных функций - {massive}')