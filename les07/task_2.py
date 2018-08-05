# Задание - 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

m = 10

lst = [round(random.uniform(0, 50), 2) for _ in range(m)]


def sort_merge(array):

    if len(array) <= 1:
        return array

    middle = len(array) // 2

    left = sort_merge(array[:middle])
    right = sort_merge(array[middle:])

    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

print(lst)
print(sort_merge(lst))
