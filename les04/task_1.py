# Задание - 1.
# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего
# задания первых трех уроков.
import random
import timeit
import cProfile


def func_1(n):
    massive = [random.randint(-n, n) for _ in range(n//3)]
    min_el = n
    max_el = -n

    for idx, el in enumerate(massive):
        if min_el > el:
            min_el = el
            min_idx = idx
        if max_el < el:
            max_el = el
            max_idx = idx

    massive[min_idx], massive[max_idx] = massive[max_idx], massive[min_idx]



# 1000 loops, best of 5: 549 usec per loop      1000
# 1000 loops, best of 5: 1.12 msec per loop     2000
# 1000 loops, best of 5: 11.7 msec per loop     20000
#
#         1    0.001    0.001    0.017    0.017 task_1.py:9(func_1)
# cProfile.run('func_1(20000)')

num = 'num1234567890123456789012345678901234567890num1234567890123456789012345678901234567890' \
      'num1234567890123456789012345678901234567890'


def func_2(n):

    def contra_num_rec(n):

        if len(n) == 1:
            return n[0]

        if len(n) == 2:
            return n[-1] + n[0]

        return n[-1] + contra_num_rec(n[1:len(n) - 1]) + n[0]
    return contra_num_rec(n)

# 1000 loops, best of 5: 963 nsec per loop  'num'
# 1000 loops, best of 5: 13 usec per loop   'num1234567890123456789012345678901234567890'
# 1000 loops, best of 5: 38.5 usec per loop 'num1234567890123456789012345678901234567890
#                                            num1234567890123456789012345678901234567890
#                                            num1234567890123456789012345678901234567890')
#
#
#    65/1    0.000    0.000    0.000    0.000 task_1.py:44(contra_num_rec)
#
# cProfile.run('func_2(num)')

def func_3(width, n):
    matrix = [[random.randint(-width, width) for _ in range(n)] for _ in range(n)]
    min_column = [width] * len(matrix)

    for line in matrix:
        for idx, el in enumerate(line):
            if el < min_column[idx]:
                min_column[idx] = el

# 100 loops, best of 5: 183 usec per loop   100000, 10
# 100 loops, best of 5: 4.25 msec per loop  100000, 50
# 100 loops, best of 5: 17.1 msec per loop  100000, 100
#
#
#         1    0.001    0.001    0.023    0.023 task_1.py:61(func_3)
# cProfile.run('func_3(100000, 100)')
