# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают
# стипендию и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%,
# кроме первого месяца. Составьте программу расчета суммы денег, которую необходимо получить
# у родителей один раз в начале обучения, чтобы можно было прожить учебный год (10 месяцев),
# используя только эти деньги и стипендию.


educational_grant = int(input('Введите стипендию: '))
sum_ed = 0  # сумма дохода
expenses = int(input('Введите расходы: '))
sum_ex = 0  # сумма расхода
for mounth in range(0, 10):
    percent = sum_ex * 3 // 100
    sum_ex = sum_ex + expenses + percent
    print(sum_ex)
    sum_ed += educational_grant
    print(sum_ed)
    print(mounth + 1)
    sum_total = sum_ex - sum_ed
print('у родителей попросить: ', sum_total)

