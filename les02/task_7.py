# Задание - 7.
# Написать программу, доказывающую или проверяющую, что для
# множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n – любое натуральное число.

print("Введите натуральное число:")
num = int(input("num = "))
i = 0
summ_left = 0

while i <= num:
    summ_left += i
    i += 1

summ_right = num * (num + 1) / 2

if summ_left == summ_right:
    print('Доказано!')
else:
    print('Легенда разрушена!')