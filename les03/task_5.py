# Задание - 5.
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

n = 100
max_count = -100
massive = [random.randint(-100, 100) for _ in range(n)]


for idx, el in enumerate(massive):
    if el > max_count and el < 0:
        max_count = el
        idx_max_el = idx

print(f'В массиве - {massive}')
print(f'Максимальное отрицательное число = {max_count} и его позиция в массиве = {idx_max_el}')