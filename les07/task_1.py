# Задание - 1.
# Отсортировать по убыванию методом «пузырька» одномерный целочисленный
# массив, заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.
# Windows 7 64-bit

import random

m = 30

lst = [random.randrange(-100, 100) for _ in range(m)]


def sort_bubble(array):
    n = 1

    while n < len(array):

        for i in range(len(array) - n):
            swap = False

            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True

        if swap == False:
            break
        n += 1
        # print(array)


#
# \les07>python -m timeit -n 100 -s "import task_1, random"
#                                           "task_1.sort_bubble([random.randrange(-100, 100) for _ in range(20)])"

# Способ из урока
# 100 loops, best of 5: 73.3 usec per loop

# Доработанный способ, добавлена проверка "отсортирован ли массив"
# 100 loops, best of 5: 62.2 usec per loop


sort_bubble(lst)
print(lst)

