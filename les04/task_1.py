import random
import timeit
import cProfile


def func_1():
    massive = [random.randint(-10000, 10000) for _ in range(10000//3)]
    min_el = 10000
    max_el = -10000

    print(f'Начальный массив - \t\t\t{massive}')

    for idx, el in enumerate(massive):
        if min_el > el:
            min_el = el
            min_idx = idx
        if max_el < el:
            max_el = el
            max_idx = idx

    massive[min_idx], massive[max_idx] = massive[max_idx], massive[min_idx]

    print(f'Массив после замены мест - \t{massive}')

# 100 loops, best of 5: 38.5 nsec per loop      100
# 1000 loops, best of 5: 34.6 nsec per loop     1000
# 10000 loops, best of 5: 34.6 nsec per loop    10000
# 100000 loops, best of 5: 35.5 nsec per loop   100000
#
#        1    0.000    0.000    0.001    0.001 task_1.py:8(func_1)
#        1    0.000    0.000    0.001    0.001 task_1.py:9(<listcomp>)

# cProfile.run('func_1()')

num = '100000213123123123123'
def func_2(n):

    def contra_num_rec(n):

        if len(n) == 1:
            return n[0]

        if len(n) == 2:
            return n[-1] + n[0]

        return n[-1] + contra_num_rec(n[1:len(n) - 1]) + n[0]
    return contra_num_rec(n)

# 1000000 loops, best of 5: 34.6 nsec per loop  1000000
# 10000000 loops, best of 5: 39.6 nsec per loop 10000000  терминал задумывается на пару секунд
# 100000000 loops, best of 5: 35 nsec per loop  100000000 тут уже задумывается на несколько десятков секунд
#
# num = '100000'
#         1    0.000    0.000    0.000    0.000 task_1.py:36(func_2)
#       3/1    0.000    0.000    0.000    0.000 task_1.py:38(contra_num_rec)
#
# num = '100000213123123123123'
#        1    0.000    0.000    0.000    0.000 task_1.py:36(func_2)
#     11/1    0.000    0.000    0.000    0.000 task_1.py:38(contra_num_rec)
#
# cProfile.run('func_2(num)')

