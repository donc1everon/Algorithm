# Задание - 3.
# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые
# не меньше медианы, в другой – не больше ее.
#
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод
# сортировки, который не рассматривался на уроках.
import random


m = 5
lst = [random.randrange(0, 100) for _ in range(2 * m + 1)]
print(lst)

# Без использования сортировки

count = 0
end_count = len(lst) - 1
pos_median = len(lst) // 2
spam = lst[:]

while len(spam) - 1 > pos_median:
    spam.remove(min(spam))

median = min(spam)

print(f'Медиана, найденая без помощи сортировки = {median}')


# Гномья сортировка


def gnome_sort(array):
    i = 1
    j = 2
    while i < len(array):
        if array[i - 1] < array[i]:
            i = j
            j = j + 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            i = i - 1
            if i == 0:
                i = j
                j = j + 1
    return array


gnome_sort(lst)
median_2 = lst[pos_median]

print(f'Медиана, найденная с помощью гномьей сортировки = {median_2}')
print(f'Сортировка в действии - {gnome_sort(lst)}')