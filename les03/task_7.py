# Задание - 7.
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

n = 10
massive = [random.randint(1, 100) for _ in range(n)]
second_min = 100
count = 0

first_min = min(massive)

for el in massive:
    if el == first_min:
        count += 1
    if count == 2:
        second_min = el
        break
    elif el < second_min and (el != first_min or count == 2):
        second_min = el

print(massive)
print(f'Самое маленькое число - {first_min}, а это второе минимальное число {second_min}')