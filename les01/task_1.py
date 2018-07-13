# Задание - 1
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
#
# Блок - схема
# https://drive.google.com/file/d/1RI4u-DGMvbfC7f_qaUMVbSWK1Pmy7F7Q/view?usp=sharing

print('Введите трехзначное число')
a = int(input('a = '))

if 99 < a < 1000:
    a_1 = a // 100
    a_2 = a // 10 % 10
    a_3 = a % 10
    summ = a_1 + a_2 + a_3
    prod = a_1 * a_2 * a_3
    print(f'Сумма цифр числа равна - {summ}, произведение цифр - {prod}')
else:
    print('Число не верное!')