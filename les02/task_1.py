# Задание - 1.
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна
# завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно
# выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный
# знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова
# запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.

while True:
    print('Введите данные для вычисления: 2 числа и знак операции: ')
    a = int(input('a = '))
    b = int(input('b = '))
    sign = input('sign = ')
    if sign == '0':
        print('До свидания!')
        break
    else:
        while (sign != '+') and (sign != '-') and (sign != '*') and (sign != '/'):
            print('Знак введен не корректно! Введите правильный знак: ')
            sign = input('sign = ')
        while b == 0:
            print('На ноль делить нельзя! Введите другой знаменатель: ')
            b = int(input('b = '))
        if sign == '+':
            eq = a + b
            print(f'Вы ввели знак "{sign}", числа {a} и {b}. Результат = {eq}')
        elif sign == '-':
            eq = a - b
            print(f'Вы ввели знак "{sign}", числа {a} и {b}. Результат = {eq}')
        elif sign == '*':
            eq = a * b
            print(f'Вы ввели знак "{sign}", числа {a} и {b}. Результат = {eq}')
        else:
            eq = a / b
            print(f'Вы ввели знак "{sign}", числа {a} и {b}. Результат = {eq}')