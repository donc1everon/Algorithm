# Задание - 1.
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования
# предприятий, чья прибыль ниже среднего.
from collections import defaultdict

name_orgs = defaultdict()
more_avrg = defaultdict()
less_avrg = defaultdict()
n = int(input("Количество предприятий: "))
full_profit = 0
avrg_annual = 0
idx = 1

for i in range(n):
    name = input(f'Предприятие №{i+1}: ')
    name_orgs[name] = {'1 кв': float(input('1ый квартал - ')), '2 кв': float(input('2ой квартал - ')),
                       '3 кв': float(input('3ой квартал - ')), '4 кв': float(input('4ой квартал - '))}
    full_profit = name_orgs[name]['1 кв'] + name_orgs[name]['2 кв'] + name_orgs[name]['3 кв'] + name_orgs[name]['4 кв']
    name_orgs[name]['Год'] = full_profit
    avrg_annual += name_orgs[name]['Год']

avrg_annual /= n

for key, value in name_orgs.items():
    if value['Год'] >= avrg_annual:
        more_avrg[key] = value['Год']
    else:
        less_avrg[key] = value['Год']

print('\nОрганизации с доходом выше среднего:')
for key, value in more_avrg.items():
    print(f'{idx}) {key} с годовой прибылью {value}')
    idx += 1

idx = 1

print('\nОрганизации с доходом ниже среднего:')
for key, value in less_avrg.items():
    print(f'{idx}) {key} с годовой прибылью {value}')
    idx += 1
