# Задание - 8
# Определить, является введённый пользователем год високосным или нет.
#
# Блок - схема
# https://drive.google.com/file/d/1NPjmvJKo8ZSaxFtmiYdh73Bds5qti0_r/view?usp=sharing

print('Введите год:')
year = int(input('year = '))

if year % 4 == 0:
    print(f'{year} - високосный год!')

else:
    print(f'{year} - НЕ високосный год!')