ticket_qty = int(input('Сколько билетов Вы хотите приобрести: '))
sum = 0
for n in range(ticket_qty):
    age = int(input('Введите возраст {}-го посетителя: '.format(n+1)))
    if 0 <= age < 18:
        sum = sum
    elif 18 <= age < 25:
        sum += 990
    elif 25 <= age <= 120:
        sum += 1390
    else:
        print('Возраст введен некорректно.')
        break

if ticket_qty > 3:
    sum *= 0.9
print('Сумма к оплате:', int(sum), 'руб.')



