# Задание - 8.
# Посчитать, сколько раз встречается определенная цифра в
# введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом
# с клавиатуры.

print('Сколько раз хотите вводить?')
t = int(input('Количество раз = '))
print('Какую цифру хотите посчитать?')
num = int(input('Цифра = '))

i = 0
q = 0

while i < t:
    m = input('Введите число: ')
    for el in m:
        if num == int(el):
            q += 1
    i += 1

print(f'Ваше число {num}, встерчается {q} раз')