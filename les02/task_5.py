# Задание - 5.
# Вывести на экран коды и символы таблицы ASCII, начиная с символа
# под номером 32 и заканчивая 127-м включительно. Вывод выполнить
# в табличной форме: по десять пар «код-символ» в каждой строке.

lst_of_chr = []
ord = 32
string = ''
n_pair = 0

for i in range(32, 128):
    lst_of_chr.append(chr(i))

for sym in lst_of_chr:
    string = string + str(ord) + ' - ' + sym + '  |  '
    n_pair += 1
    ord += 1
    if n_pair == 10:
        print(string)
        string = ''
        n_pair = 0
print(string)