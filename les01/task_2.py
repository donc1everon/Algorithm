# Задание - 2
# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный
# результат
#
# Блок - схема
# https://drive.google.com/file/d/1lOtncTcisiubXghuvnZHF_oxrmdyYsB7/view?usp=sharing

a = 5
b = 6

print('Двиочный вид а =', bin(a), 'b =', bin(b))
print('Побитовое ИЛИ -', bin(a | b))
print('Побитовое И -', bin(a & b))
print('Побитовый сдвиг вправо -', bin(a >> 2))
print('Побитовый сдвиг влево -', bin(a << 2))
print('При сдвиге освободившиеся ячейки заполнятся нолями, 101 >> 2 = 001, 101 << 2 = 10100')