# Вы уже писали программу, вычисляющую сумму налога по прогрессивной шкале в зависимости от
# полученного заработка: 13% на доход до 10 000, 20% на доход от 10 000 до 50 000, 30% на доход выше 50 000.
# Однако во многих странах, использующих такую шкалу, эта сумма вычисляется более сложным способом:
# налоговая ставка 30% на доход выше 50 000 означает, что 30% уплачивается не со всей суммы,
# а лишь с той её части, которая превосходит 50 000. Аналогично ставка 20% на доход от 10 000
# до 50 000 обязывает уплатить 20% лишь с той части суммы, которая превосходит 10 000, но не превосходит 50 000.
# Напишите программу, которая спрашивает у пользователя его доход и высчитывает сумму налога для него по вышеописанным правилам.


profit = int(input('Введите ваш доход: '))
if profit > 50000:
    tax = (0.3 * (profit - 50000)) + (0.2 * (50000 - 10000)) + 0.13 * 10000
elif profit < 50000 and profit > 10000:
    tax = (0.2 * (profit - 10000)) + (0.13 * 10000)
else:
    tax = profit * 0.13
print('Налог составит: ', tax)
