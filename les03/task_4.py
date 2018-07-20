# Задание - 4.
# Определить, какое число в массиве встречается чаще всего.
import random

n = 100
max_count = 0
massive = [random.randint(1, 100) for _ in range(n)]

for el in massive:
    count = 0
    for i in range(n):
        if el == massive[i]:
            count += 1
        if count > max_count:
            max_count = count
            max_idx = i

print(f'В массиве - {massive}, \nчаще всего встречается это число - {massive[max_idx]}')