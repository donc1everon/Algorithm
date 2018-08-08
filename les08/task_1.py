# Задание - 1.
# Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
from hashlib import sha1

S = 'beep boop beer!'
N = len(S)


def find_all_substing(string):
    count = 0
    h_list = []

    #
    for i in range(0, N):

        for j in range(0, N):

            if j + 1 > i:
                subs = string[i:j + 1]
                h_subs = sha1(string[i:j + 1].encode("utf-8")).hexdigest()

                if h_subs not in h_list:
                    h_list.append(h_subs)
                    count += 1

    return count


print(f'Число различных подстрок в строке "{S}" = {find_all_substing(S)}')
