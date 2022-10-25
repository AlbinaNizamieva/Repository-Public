per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму:'))
val = per_cent.values()
deposit = []
for item in val:
    d = money * item / 100
    deposit.append(d)
print('deposit -', deposit)
print('Максимальная сумма, которую вы можете заработать —', max(deposit))