# Задание - 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
#
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

int_16 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
number_1 = list(input('Введите число №1 в 16-ричной системе: ').upper())
number_2 = list(input('Введите число №2 в 16-ричной системе: ').upper())


def get_key_from_dict(dict, num):
    for key, value in dict.items():
        if value == num:
            return key


def summ(n1, n2):
    result = []
    i = 1
    eggs = 0

    if len(n1) < len(n2):
        while len(n1) != len(n2):
            empty_slot = ['0']
            n1 = empty_slot + n1
    else:
         while len(n1) != len(n2):
            empty_slot = ['0']
            n2 = empty_slot + n2

    while i < (len(n1) + 1):
        summ_ = int_16[n1[len(n1) - i]] + int_16[n2[len(n2) - i]] + eggs
        eggs = 0

        if summ_ < 16:
            result.append(get_key_from_dict(int_16, summ_))
        else:
            summ_ = summ_ - 16
            result.append(get_key_from_dict(int_16, summ_))
            eggs += 1

        i += 1

        if eggs != 0 and i == len(n1) + 1:
            result.append(get_key_from_dict(int_16, eggs))
    result = result[::-1]

    return result


def multi(n3, n4):
    for_summ = {}


    n3 = n3[::-1]
    n4 = n4[::-1]
    for idx, num1 in enumerate(n3):
        result_multi_by_one = []
        eggs = 0

        for num2 in n4:
            multi = int_16[num1] * int_16[num2] + eggs
            eggs = 0
            if multi < 16:
                result_multi_by_one.append(get_key_from_dict(int_16, multi))
            else:
                while multi > 15:
                    multi = multi - 16
                    eggs += 1
                result_multi_by_one.append(get_key_from_dict(int_16, multi))

        if len(n4) > len(n3) and n4.index(num2) == (len(n4) - 1):
            result_multi_by_one.append(get_key_from_dict(int_16, eggs))
        elif len(n4) < len(n3) and n4.index(num2) == (len(n4) - 1):
            result_multi_by_one.append(get_key_from_dict(int_16, eggs))
        elif len(n4) == len(n3) and n4.index(num2) == (len(n4) - 1):
            result_multi_by_one.append(get_key_from_dict(int_16, eggs))

        result_multi_by_one = result_multi_by_one[::-1]
        last_empty_slot = ['0'] * idx

        if last_empty_slot != '':
            result_multi_by_one += last_empty_slot
        for_summ[idx] = result_multi_by_one
        len_ = len(for_summ)

    result_multi = ['0']

    while len_ > 0:
        result_multi = summ(result_multi, for_summ[len_ - 1])
        len_ -= 1

    return result_multi


print(multi(number_1, number_2))
print(summ(number_1, number_2))
