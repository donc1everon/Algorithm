# Задание - 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.
import cProfile

index_int = int(input("¬ведите какое по счету простое число хотите видеть: "))


def erato(n):
    while True:
        sieve = [i for i in range(n)]
        sieve[1] = 0

        for i in range(2, n):
            if sieve != 0:
                j = i * 2
                while j < n:
                    sieve[j] = 0
                    j += i

        sieve = [i for i in sieve if i != 0]

        if len(sieve) < index_int:
            n += n
        else:
            break
    return sieve[index_int -  1]

print(erato(index_int))



# 10000 loops, best of 5: 26.4 usec per loop    10
# 10000 loops, best of 5: 75.7 usec per loop    25
# 10000 loops, best of 5: 425 usec per loop     50
#
#         1    0.001    0.001    0.001    0.001 task_2.py:10(erato)
#
# cProfile.run("erato(index_int)")


def erato_2(num):

    def check_prime(num):

        if (num == 1):
            return 0
        elif (num == 2):
            return num
        else:
            for i in range(2, num):
                if(num % i == 0):
                    return 0
            return num

    lst_ = [check_prime(i) for i in range(num) if check_prime(i) != 0]

    if (index_int - 1) > len(lst_):
        num += num
        return erato_2(num * 3)
    elif index_int <= len(lst_):
        return lst_[index_int - 1]
    else:
        return -1
    
print(erato_2(index_int))


# 10000 loops, best of 5: 89.3 usec per loop    10
# 10000 loops, best of 5: 344 usec per loop     25
# 10000 loops, best of 5: 1.08 msec per loop    50

#       2/1    0.000    0.000    0.006    0.006 task_2.py:44(erato_2)
#      1021    0.005    0.000    0.005    0.000 task_2.py:46(check_prime)
#
# cProfile.run("erato_2(index_int)")

