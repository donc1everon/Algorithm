# Задание - 9.
# Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр. Вывести на экран
# это число и сумму его цифр.
num = 0
summ = 0
max_s = 0
max_num = 0

print("Вводите пока не надоест вводить:")
while num != '000':
    print('Для выхода введите 000')
    num = input('num = ')
    for el in num:
        summ += int(el)
    if max_s < summ:
        max_s = summ
        max_num = num
    summ = 0

print(f'Наибольшее по сумме цифр - {max_num}, его сумма = {max_s}')

