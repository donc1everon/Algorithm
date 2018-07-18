# Задание - 3.
# Сформировать из введенного числа обратное по порядку входящих в него цифр и
# вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

print('Введите число:')
num = input('num = ')
contra_num = ''

for n in num:
    contra_num = n + contra_num

print(f'Вариант - 1. Число наоборот = {contra_num}')


num = num[::-1]
print(f'Вариант - 2. Число наоборот = {num}')


def contra_num_rec(n):

    if len(n) == 1:
        return n[0]

    if len(n) == 2:
        return n[-1] + n[0]

    return n[-1] + contra_num_rec(n[1:len(n) - 1]) + n[0]

print(contra_num_rec(num))
